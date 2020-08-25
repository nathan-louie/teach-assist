"""
"""

from src.log import create_logger
from bs4 import BeautifulSoup
import re

logger = create_logger(__name__)

class Parse:
    """
    """
    def __init__(self, text: str) -> None:
        """
        >>>
        """
        self.html = BeautifulSoup(text, 'html.parser')
        self.names = []
        self.location = []
        self.link = []
        self.current_mark = []

    def search(self) -> None:
        """
        >>>
        """
        for td in self.html.select('td'):
            if ':' in td.text and '-' in td.text:
                for part in td.text.split('\n'):
                    temp = re.sub('\t', '', part)

                    if temp is '':
                        continue

                    if 'rm.' in part:
                        self.location.append(temp.strip())
                    else:
                        self.names.append(temp.strip())
    
        for report in self.html.select('a[href^="viewReport.php?"]'):
            self.link.append(report['href'].strip())
            self.currentMark.append(report.text.strip())


def main() -> None:
    """
    """
    logger.info('parse.py ran as main.')
    import doctest
    doctest.testmod()
    logger.info('doctest ran.')

if __name__ == '__main__':
    main()