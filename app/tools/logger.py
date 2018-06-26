# This Python file uses the following encoding: utf-8
import logging
from logging.handlers import TimedRotatingFileHandler

from config import Config


class Logger:
    def __init__(self, logname, loglevel, logger=''):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """

        # 创建一个logger
        if logger:
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.NOTSET)
        else:
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.NOTSET)

        # 创建一个handler，用于写入日志文件,并指定文件写入方式
        fh = logging.FileHandler(logname, 'a')
        filehandler = logging.handlers.TimedRotatingFileHandler(logname, 'midnight', 1)
        self.logger.addHandler(filehandler)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()

        fh.setLevel(Config.logger_level[int(loglevel)])
        ch.setLevel(Config.logger_level[int(loglevel)])
        ''' Python 2.X不支持filter方法
        if loglevel:
            if loglevel == 5:
                fh.addFilter(lambda record: 'ERROR' in record.levelname)
            elif loglevel == 4:
                fh.addFilter(lambda record: 'WARNING' in record.levelname)
            elif loglevel == 3:
                fh.addFilter(lambda record: 'INFO' in record.levelname)
            elif loglevel == 2:
                fh.addFilter(lambda record: 'DEBUG' in record.levelname)
        '''
        # 定义handler的输出格式
        formatter = Config.format_dict
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # self.logger.removeHandler(fh)
        # self.logger.removeHandler(ch)

    def getlog(self):
        return self.logger

# 调用示例
    '''
    SysLog().get_errorlog().error('error')
    '''
