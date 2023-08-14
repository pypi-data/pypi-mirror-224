from django.utils.deprecation import MiddlewareMixin

from djangolin.repo.tools.loggers import logger


class LoggerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        logger('set')
        logger().set_request(request)

    def process_response(self, request, response):
        logger().set_response(response)
        return response
