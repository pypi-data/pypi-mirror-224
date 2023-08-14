from threading import local

from .__logger import Logger

__local = local()


def logger(reset=False, debug=True):
    if reset or not hasattr(__local, 'logger'):
        __local.logger = Logger(debug=True)

    return __local.logger
