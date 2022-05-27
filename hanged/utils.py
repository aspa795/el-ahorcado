import logging

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_response(url, path):
    response = requests.get(
        url=url + path,
    )

    if response.status_code != 200:
        logger.error(
            str(response.text),
            exc_info=True,
            extra={"url": url + path},
        )

    return response
