"""
unittest class to test get_data.py.
"""

import unittest

from src import get_data
from src.log import create_logger

logger = create_logger(__name__)

class TestData(unittest.TestCase):
    def testPostGoodResponse(self):
        """
        """
        pass

    def testPostBadResponse(self):
        """
        """
        pass

    def testPostUnsuccessful(self):
        """
        """
        pass

def main() -> None:
    logger.info('test_get_data.py rain as main.')
    unittest.main()

if __name__ == '__main__':
    main()