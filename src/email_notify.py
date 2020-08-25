"""
"""

import os
import ssl
import smtplib

from src.log import create_logger

PORT = 465
SMTP_SERVER = 'smtp.gmail.com'
FILE = 'email_credentials.txt'
TEXT_FILE_DIRECTORY = 'data-files'

logger = create_logger(__name__)
context = ssl.create_default_context()

class Email:
    """
    """
    def __init__(self, message: str) -> None:
        """
        >>>
        """
        self.message = message
        try:
            with open(os.path.join(TEXT_FILE_DIRECTORY, FILE)) as file:
                self.__user = file.readline()
                self.__password = file.readline()
            logger.info('Successfully found credentials.')
                
        except Exception as exception:
            exception_msg = str(exception)
            logger.exception('Exception during file reading: {0}'.format(exception_msg))
    
    def send(self) -> None:
        """
        >>>
        """
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
                server.login(self.__user, self.__password)
                server.sendmail(self.__user, self.__user, self.message)
                logger.info('Successfully sent email.')

        except smtplib.SMTPResponseException as exception:
            exception_code = str(exception.smtp_code)
            exception_error = str(exception.smtp_error)
            logger.exception('Exception during email, returned error code: {0}, with message: {1}'.format(exception_code, exception_error))

def main() -> None:
    logger.info('email_notify.py ran as main.')
    import doctest
    doctest.testmod(extraglobs={'email': Email('doctest ran.')})
    logger.info('doctest ran.')

if __name__ == '__main__':
    main()