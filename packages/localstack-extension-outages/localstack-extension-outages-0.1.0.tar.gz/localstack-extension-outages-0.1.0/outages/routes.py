import json,logging,threading
from jsonschema import ValidationError,validate
from localstack.http import Request,Response
from outages.config import OUTAGE_CONFIG,OUTAGE_CONFIG_SCHEMA
OUTAGE_CONFIG_LOCK=threading.Lock()
def handle_get_config(request,**A):return Response.for_json(OUTAGE_CONFIG,status=200)
def handle_put_config(request,**F):
	C='error'
	try:
		with OUTAGE_CONFIG_LOCK:B=json.loads(request.data);validate(instance=B,schema=OUTAGE_CONFIG_SCHEMA);OUTAGE_CONFIG.update(B);return Response.for_json(OUTAGE_CONFIG,status=200)
	except json.JSONDecodeError as A:D={C:f"Invalid JSON: {A}"};logging.debug(f"Error decoding JSON: {A}");return Response.for_json(D,status=400)
	except ValidationError as A:E={C:f"Error in validation: {A.message}"};logging.debug(f"Error validating JSON schema: {A.message}");return Response.for_json(E,status=400)