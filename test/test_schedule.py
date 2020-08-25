"""
"""

import unittest

from src import schedule
from src.log import create_logger

logger = create_logger(__name__)

class TestSchedule:
    def test(self):
        """
        """
        pass

def main() -> None:
    logger.info('test_schedule.py rain as main.')
    unittest.main()

if __name__ == '__main__':
    main()