"""
unittest class to test email_notify.py.
"""

import unittest

from src import email_notify
from src.log import create_logger

logger = create_logger(__name__)

class TestEmail(unittest.TestCase):
    def testSendEmail(self) -> None:
        """
        Test the email sending functionality.
        -> Assert the log message and status.
        """
        with self.assertLogs('email_notify', 'INFO') as cm:
            notify = email_notify.Email('test.py ran (unittest)')
            notify.send()
        self.assertEqual(cm.output, ['INFO:email_notify:Successfully sent email.'], 'Email notification not sent.')
    
    def testSMTPPort(self) -> None:
        """
        Test the correct SMTP port is used.
        -> Assert the port value.
        """
        port = email_notify.PORT
        self.assertEqual(port, 465, 'Incorrect SMTP port found.')

    def testSMTPServer(self) -> None:
        """
        Test the correct SMTP server is used.
        -> Assert the SMTP server string.
        """
        smtp_server = email_notify.SMTP_SERVER
        self.assertEqual(smtp_server, 'smtp.gmail.com', 'Incorrect SMTP server found.')

def main() -> None:
    logger.info('test_email_notify.py rain as main.')
    unittest.main()

if __name__ == '__main__':
    main()