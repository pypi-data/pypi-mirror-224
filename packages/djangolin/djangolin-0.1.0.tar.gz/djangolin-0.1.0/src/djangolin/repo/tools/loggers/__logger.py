from datetime import datetime
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from djangolin.models import (
    RequestModel,
    RequestPropertyModel,
    LogModel,
    ResponseModel,
    ResponsePropertyModel,
)

ERROR = 'ERROR'
WARNING = 'WARNING'
DEBUG = 'DEBUG'
EXCEPTION = 'EXCEPTION'
INFO = 'INFO'


class Log:
    __repository: list = list()

    __error_messages: list = list()
    __warning_messages: list = list()
    __debug_messages: list = list()
    __exception_messages: list = list()
    __info_messages: list = list()

    def error(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': ERROR,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )
        self.__error_messages.append(message)

    def warning(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': WARNING,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )
        self.__warning_messages.append(message)

    def debug(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': DEBUG,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )
        self.__debug_messages.append(message)

    def exception(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': EXCEPTION,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )
        self.__exception_messages.append(message)

    def info(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': INFO,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )
        self.__info_messages.append(message)

    def export(self):
        return self.__repository

    def messages(self, debug=True):
        ret = {
            'error': self.__error_messages,
            'warning': self.__warning_messages,
            'debug': self.__debug_messages if debug else [],
            'exception': self.__exception_messages if debug else [],
            'info': self.__info_messages,
        }
        return ret


class Logger:

    def __init__(self, debug=True):
        self.__debug = debug

    __request: dict | None = None

    def set_request(self, value: HttpRequest):
        self.__request = {
            'path': value.path,
            'datetime': datetime.now(),
            'extra': {}
        }

    log: Log = Log()

    __response: dict | None = None

    def set_response(self, value: HttpResponse):
        self.__response = {
            'status_code': value.status_code,
            'datetime': datetime.now(),
            'extra': {},
        }
        self.__add_to_db()

    def __add_to_db(self):
        self.__request_add_to_db()
        self.__logs_add_to_db()
        self.__response_add_to_db()

    __request_obj = None

    def __request_add_to_db(self):
        inst = RequestModel(**self.__request)
        inst.save()
        self.__request_obj = inst

    def __logs_add_to_db(self):
        LogModel.objects.bulk_create(
            [LogModel(request=self.__request_obj, **i) for i in self.log.export()])

    def __response_add_to_db(self):
        inst = ResponseModel(request=self.__request_obj, **self.__response)
        inst.save()

    def messages(self):
        return self.log.messages(self.__debug)
