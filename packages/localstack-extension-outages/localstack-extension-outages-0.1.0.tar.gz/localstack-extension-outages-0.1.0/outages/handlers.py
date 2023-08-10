import logging
from localstack.aws.api import RequestContext
from localstack.aws.chain import Handler,HandlerChain
from localstack.http import Response
from outages.config import OUTAGE_CONFIG
from outages.exceptions import ServiceUnavailableException
LOG=logging.getLogger(__name__)
class OutageHandler(Handler):
	def __call__(B,chain,context,response):
		A=context
		if A.is_internal_call:return
		if A.service.service_name in OUTAGE_CONFIG.get('services',[]):raise ServiceUnavailableException('Service not accessible (LocalStack Outages Extension)')
		if A.region in OUTAGE_CONFIG.get('regions',[]):raise ServiceUnavailableException('Region not accessible (LocalStack Outages Extension)')