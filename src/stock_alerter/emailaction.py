# encoding:UTF-8

import smtplib
from email.mime.text import MIMEText


########################################################################
class EmailAction:
    """Send an email when a rule is matched"""
    from_email = "alerts@stocks.com"

    #----------------------------------------------------------------------
    def __init__(self, to):
        """Constructor"""
        self.to_email = to
        
    #----------------------------------------------------------------------
    def execute(self, content):
        """"""
        message = MIMEText(content)
        message["Subject"] = "New Stock Alert"
        message["From"] = "alerts@stocks.com"
        message["To"] = self.to_email
        smtp = smtplib.SMTP("email.stocks.com")
        try:
            smtp.send_message(message)
        finally:
            smtp.quit()        
    