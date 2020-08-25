import unittest
import log
import parse

logger = log.setup_custom_logger(__name__)

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