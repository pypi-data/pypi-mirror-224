import logging
from typing import Optional

import requests
from retrying import retry

logger = logging.getLogger(__name__)


NEWLINE = '\n'

class JSONDecodingError(Exception):
    ...

class RequestFailedException(Exception):
    ...


@retry(retry_on_exception=lambda exception: isinstance(exception, RequestFailedException),
       stop_max_delay=5 * 60 * 1000, # 5 minutes
       wait_exponential_multiplier=1000, # 1 second
       wait_exponential_max=60 * 1000) # 1 minute in milliseconds
def get_json(url: str, query_parameters: Optional[dict] = None,  headers: Optional[dict] = None):
    response = requests.get(
        url,
        params=query_parameters,
        headers=headers
    )
    if not (200 <= response.status_code < 300):
        error_message = f'Request failed with status {response.status_code}:{NEWLINE}{response.text}'
        logger.error(error_message)
        raise RequestFailedException(error_message)

    logger.info(f'Request succeeded with status {response.status_code}')

    try:
        json_data = response.json()
    except Exception as e:
        logger.error(str(e))
        error_message = f'Failed to parse JSON from: {response.text}'
        logger.error(error_message)
        raise JSONDecodingError(error_message)

    return json_data
