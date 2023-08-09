
import logging
import logging.config
import os
import queue
import threading
import copy
import time
from logging.handlers import QueueHandler, QueueListener

from utils import get_log_default_path, get_digit_from_env, get_log_given_path


class Logger:

    LogHandlerSample = {
        'console': {
            'level': None,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': None,
            'class': None,
            'filename': None,
            'formatter': 'standard',
            'encoding': 'utf-8',
            'backupCount': None
        }
     }

    LogConfigLock = threading.Lock()
    LogConfig = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'filters': {
        },
        'handlers': {
        },
        'loggers': {
        }
    }

    @classmethod
    def _get_log_level_from_env(cls, env_name, default_level=logging.DEBUG):
        log_level = str(os.environ.get(env_name)).lower()

        if log_level == "off":
            return logging.CRITICAL
        elif log_level == "critical":
            return logging.CRITICAL
        elif log_level == "err":
            return logging.ERROR
        elif log_level == "warn":
            return logging.WARNING
        elif log_level == "info":
            return logging.INFO
        elif log_level == "debug":
            return logging.DEBUG
        elif log_level == "trace":
            return logging.NOTSET
        else:
            return default_level

    @classmethod
    def _get_log_path_from_env(cls, path):
        log_path = get_log_given_path(path)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        if not os.path.isdir(log_path):
            raise TypeError("The log path '{}' is not a directory.".format(log_path))
        return log_path

    @classmethod
    def get_logger(cls, name, path, async_logging=True):
        with cls.LogConfigLock:
            cls.LogConfig['handlers'][f'file_{name}'] = copy.deepcopy(cls.LogHandlerSample['file'])
            cls.LogConfig['handlers'][f'console_{name}'] = copy.deepcopy(cls.LogHandlerSample['console'])

            if str(os.environ.get('USE_TIMED_LOG')).lower() == 'false':
                cls.LogConfig['handlers'][f'file_{name}']['class'] = 'logging.handlers.RotatingFileHandler'
                cls.LogConfig['handlers'][f'file_{name}']['maxBytes'] = get_digit_from_env('FILE_MAX_BYTES', 1073741824)  # 1GB = 1024 * 1024 * 1024
            else:
                cls.LogConfig['handlers'][f'file_{name}']['class'] = 'logging.handlers.TimedRotatingFileHandler'
                cls.LogConfig['handlers'][f'file_{name}']['when'] = 'MIDNIGHT'
                cls.LogConfig['handlers'][f'file_{name}']['interval'] = 1

            filename = name + time.strftime("%Y%m%d%H%M%S", time.localtime())
            cls.LogConfig['handlers'][f'file_{name}']['filename'] = os.path.join(cls._get_log_path_from_env(path), f'{filename}.log')
            cls.LogConfig['handlers'][f'console_{name}']['level'] = cls._get_log_level_from_env('CONSOLE_LOG_LEVEL', logging.ERROR)
            cls.LogConfig['handlers'][f'file_{name}']['level'] = cls._get_log_level_from_env('FILE_LOG_LEVEL', logging.INFO)
            cls.LogConfig['handlers'][f'file_{name}']['backupCount'] = get_digit_from_env('FILE_BACKUP_COUNT', 21)

            cls.LogConfig['loggers'][name] = {}
            cls.LogConfig['loggers'][name]['handlers'] = [f'file_{name}', f'console_{name}']
            cls.LogConfig['loggers'][name]['level'] = 'DEBUG'
            log_config = copy.deepcopy(cls.LogConfig)

        logging.config.dictConfig(log_config)
        if async_logging:
            return cls.make_handlers_async(name)
        else:
            return logging.getLogger(name)

    @staticmethod
    def _select_and_disable_console_handler(hdlrs):
        for hdlr in hdlrs:
            if hdlr.name.startswith('console_'):
                hdlr.setStream(open('/dev/null', 'w'))
            if isinstance(hdlr, QueueHandler):
                Logger._select_and_disable_console_handler(hdlr.listener.handlers)

    @classmethod
    def redirect_console_handler_to_DEVNULL(cls):
        # root_logger = logging.getLogger()
        with cls.LogConfigLock:
            loggers = [one for one in cls.LogConfig['loggers'].keys() if one != '']

        for l_name in loggers:
            logger = logging.getLogger(l_name)
            Logger._select_and_disable_console_handler(logger.handlers)

    @classmethod
    def make_handlers_async(cls, l_name: str):
        ''' wrap the logger's handlers with a queued handler '''
        # root_logger = logging.getLogger()
        logger = logging.getLogger(l_name)
        assert not any([isinstance(h, QueueHandler) for h in logger.handlers]), 'exists handlers which have already been made async'
        q = queue.Queue()
        qhandler = QueueHandler(q)
        qhandler.listener = QueueListener(q, *logger.handlers, respect_handler_level=True)
        qhandler.listener.start()
        logger.handlers = [qhandler]
        return logger

    @classmethod
    def stop(cls):
        cls.stop_async_handlers()

    @classmethod
    def stop_async_handlers(cls):
        ''' stop queued handler and flush all pending logs '''
        # root_logger = logging.getLogger()
        with cls.LogConfigLock:
            loggers = [one for one in cls.LogConfig['loggers'].keys() if one != '']

        for l_name in loggers:
            logger = logging.getLogger(l_name)
            for hdlr in logger.handlers:
                if isinstance(hdlr, QueueHandler) and hdlr.listener is not None:
                    hdlr.listener.stop()
                    hdlr.listener = None
