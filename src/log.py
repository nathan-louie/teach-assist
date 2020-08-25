"""
"""

import logging

def create_logger(name: str) -> logging.getLogger():
    """
    >>>
    """
    formatter = logging.Formatter(fmt='\n%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def main() -> None:
    """
    """
    logger = create_logger(__name__)
    logger.info('log.py ran as main.')
    import doctest
    doctest.testmod()
    logger.info('doctest ran.')
    
if __name__ == '__main__':
    main()