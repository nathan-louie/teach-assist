"""
"""

import unittest

from src import parse
from src.log import create_logger

logger = create_logger(__name__)

class TestLog:
    def test(self):
        """
        """
        pass

def main() -> None:
    logger.info('test_parse.py rain as main.')
    unittest.main()

if __name__ == '__main__':
    main()