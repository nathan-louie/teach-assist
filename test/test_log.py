import unittest
import log

logger = log.setup_custom_logger(__name__)

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