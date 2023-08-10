import logging
from localstack.aws.chain import CompositeHandler
from localstack.extensions.api import Extension
from localstack.extensions.api.http import RouteHandler,Router
from outages.constants import CONFIG_ENDPOINT,CONFIG_PATH
from outages.handlers import OutageHandler
from outages.routes import handle_get_config,handle_put_config
LOG=logging.getLogger(__name__)
class OutagesExtension(Extension):
	name='outages'
	def update_gateway_routes(B,router):A=router;A.add(CONFIG_PATH,handle_get_config,methods=['GET'],host=CONFIG_ENDPOINT);A.add(CONFIG_PATH,handle_put_config,methods=['PUT'],host=CONFIG_ENDPOINT)
	def update_request_handlers(A,handlers):handlers.handlers.append(OutageHandler())