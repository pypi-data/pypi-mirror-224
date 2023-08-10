_A=False
from localstack.aws.api import ServiceException
class BadGatewayException(ServiceException):code='BadGatewayException';sender_fault=_A;status_code=502
class ServiceUnavailableException(ServiceException):code='ServiceUnavailableException';sender_fault=_A;status_code=503;retryAfterSeconds='10'
class GatewayTimeoutException(ServiceException):code='GatewayTimeoutException';sender_fault=_A;status_code=504