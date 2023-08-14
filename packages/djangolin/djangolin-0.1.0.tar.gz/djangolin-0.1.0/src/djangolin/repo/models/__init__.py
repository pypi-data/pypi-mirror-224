from .__request import Request as RequestModel
from .__request_property import RequestProperty as RequestPropertyModel
from .__log import Log as LogModel
from .__response import Response as ResponseModel
from .__response_property import ResponseProperty as ResponsePropertyModel


class LoggerDBRouter(object):
    DEFAULT = 'default'
    LOGGER_DB = 'logger_db'

    @property
    def __model_list(self):
        ret = [
            RequestModel,
            RequestPropertyModel,
            LogModel,
            ResponseModel,
            ResponsePropertyModel,
        ]
        return ret

    @property
    def __model_name_list(self):
        ret = [c.__name__.lower() for c in self.__model_list]
        return ret

    def db_for_read(self, model, **hints):
        ret = self.LOGGER_DB if model in self.__model_list else self.DEFAULT
        return ret

    def db_for_write(self, model, **hints):
        ret = self.LOGGER_DB if model in self.__model_list else self.DEFAULT
        return ret

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        ret = self.LOGGER_DB == db if model_name in self.__model_name_list else self.DEFAULT == db
        return ret
