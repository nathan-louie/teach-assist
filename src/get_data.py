"""
"""

import requests
import contextlib
import time

from src.log import create_logger

logger = create_logger(__name__)

class Retrieve:
    """
    """
    def __init__(self, url: str, params: dict) -> None:
        """
        >>>
        """
        self.url = url
        self.params = params

    def post(self) -> str:
        """
        >>>
        """
        for i in range (1, 4):
            try:
                with contextlib.closing(requests.post(self.url, data=self.params)) as response:
                    is_good = self.__is_good_response
                    logger.info('Made request, received {0} response.'.format('GOOD' if is_good else 'BAD'))
                    return response if is_good else ''

            except requests.exceptions.RequestException as exception:
                logger.exception('Exception during request to {0}: {1}'.format(self.url, str(exception)))
                logger.info('Retry request... ({0} of 3)'.format(i))
                if i == 3:
                    logger.error('Request unsuccessful, try again later.')
                else:
                    time.sleep(2)

    @staticmethod
    def __is_good_response(response: str) -> bool:
        """
        >>>
        """
        content_type = response.headers['Content-Type'].lower()
        return (response.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def main() -> None:
    """
    """
    logger.info('get_data.py ran as main.')
    import doctest
    doctest.testmod(extraglobs={'carrier': Retrieve('', {})})
    logger.info('doctest ran.')

if __name__ == '__main__':
    main()