"""
"""

import unittest

from src.log import create_logger

logger = create_logger(__name__)

class TestLog:
    def testSetupCustomLogger(self):
        """
        """
        pass

def main() -> None:
    logger.info('test_log.py rain as main.')
    unittest.main()

if __name__ == '__main__':
    main()