# This Python file uses the following encoding: utf-8
# 系统日志配置方法
from app.tools.logger import Logger
from config import Config


class SysLog:
    @staticmethod
    def get_errorlog():
        errorlogger = Logger(logname=Config.logger_error, loglevel=5, logger=__name__).getlog()
        return errorlogger

    @staticmethod
    def get_warninglog():
        warninglogger = Logger(logname=Config.logger_warning, loglevel=4, logger=__name__).getlog()
        return warninglogger

    @staticmethod
    def get_infolog():
        infologger = Logger(logname=Config.logger_info, loglevel=3, logger=__name__).getlog()
        return infologger

    @staticmethod
    def get_debuglog():
        debuglogger = Logger(logname=Config.logger_debug, loglevel=2, logger=__name__).getlog()
        return debuglogger

    @staticmethod
    def get_weblog():
        weblogger = Logger(logname=Config.logger_weblog, loglevel=3,).getlog()
        return weblogger
