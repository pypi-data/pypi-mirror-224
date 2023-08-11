import os, sys, threading, queue, datetime
from typing import Optional, Set

from CheeseType import NonNegativeInt

class Level:
    def __init__(self, weight: NonNegativeInt, color: Optional[str] = None, messageTemplate: Optional[str] = None):
        '''
        ### Args

        - weight：权重。小于日志过滤权重的消息会被忽略。

        - color：控制台打印的等级标签样式。

        - messageTemplate：消息格式，默认为`logger.messageTemplate`。
        '''

        self.weight: NonNegativeInt = weight
        self.color: Optional[str] = color
        self.messageTemplate: Optional[str] = messageTemplate

class Logger(threading.Thread):
    def __init__(self):
        self.filePath: Optional[str] = None
        self.messageTemplate: str = '(%level) %Y-%m-%d %H:%M:%S.%f > %content'
        self.filter: NonNegativeInt | Set[str] = set()
        self.levels: dict[str, Level] = {
            'DEBUG': Level(10, '34', None),
            'INFO': Level(20, '32', None),
            'STARTING': Level(20, '32', None),
            'LOADING': Level(20, '34', '(%level) %content'),
            'LOADED': Level(20, '35', None),
            'ENDING': Level(20, '34', None),
            'HTTP': Level(20, '34', None),
            'WEBSOCKET': Level(20, '34', None),
            'WARNING': Level(30, '33', None),
            'DANGER': Level(40, '31', None),
            'ERROR': Level(50, '35', None)
        }
        self.colorful: bool = True
        self._queue: queue.Queue = queue.Queue()
        self._flag: bool = False

        super().__init__(daemon = True)

    def run(self):
        self._flag = True
        while self._flag or not self._queue.empty():
            level, now, message = self._queue.get()
            message = now.strftime((self.levels[level].messageTemplate or self.messageTemplate).replace('%level', level).replace('%content', message).replace('\n', '\n    ')) + '\n'
            if self.filePath is not None:
                os.makedirs(os.path.dirname(self.filePath), exist_ok = True)
                with open(self.filePath, 'a', encoding = 'utf-8') as f:
                    f.write(message)

    def stop(self):
        self._flag = False
        self.join()

logger = Logger()

def default(level: str, message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    ''' Validate '''
    if level not in logger.levels:
        raise KeyError('no level with this key')

    ''' Filter '''
    if isinstance(logger.filter, set):
        for _level in logger.filter:
            if level == _level:
                return
    elif logger.levels[level].weight <= NonNegativeInt(logger.filter):
        return

    ''' Terminal '''
    now = datetime.datetime.now()
    message = f'{message}'
    if sys.stdout.isatty():
        if logger.colorful:
            terminalMessage = now.strftime((logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', f'\033[{logger.levels[level].color}m{level}\033[0m' if logger.levels[level].color else level).replace('%content', colorfulMessage or message).replace('\n', '\n    '))
        else:
            terminalMessage = now.strftime((logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', level).replace('%content', message).replace('\n', '\n    '))
        print(terminalMessage)

    ''' Log file writter '''
    if logger.filePath is not None:
        if not logger.is_alive():
            logger.start()
        logger._queue.put((level, now, message))

def debug(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('DEBUG', message, colorfulMessage, logger)

def info(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('INFO', message, colorfulMessage, logger)

def starting(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('STARTING', message, colorfulMessage, logger)

def ending(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('ENDING', message, colorfulMessage, logger)

def warning(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('WARNING', message, colorfulMessage, logger)

def danger(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('DANGER', message, colorfulMessage, logger)

def error(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('ERROR', message, colorfulMessage, logger)

def http(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('HTTP', message, colorfulMessage, logger)

def websocket(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('WEBSOCKET', message, colorfulMessage, logger)

def loaded(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('LOADED', message, colorfulMessage, logger)

def loading(message: str, logger: Optional[Logger] = logger, end: str | None = '\n'):
    if sys.stdout.isatty():
        message = f'{message}'
        terminalMessage = (logger.levels['LOADING'].messageTemplate or logger.messageTemplate).replace('%level', f'\033[{logger.levels["LOADING"].color}mLOADING\033[0m').replace('%content', message).replace('\n', '\n    ')
        print(terminalMessage, end = end)
