import datetime
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

from settings.settings import smtp_server, mail_login, mail_passwd, receiver, cc

today = datetime.date.today().strftime('%d.%m.%Y')
excel_file = 'Oplata_polzovateley_' + today + '.xlsx'


def send_mail():
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(excel_file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(excel_file))

    # Compose message
    msg = MIMEMultipart()
    msg['From'] = mail_login
    msg['To'] = ', '.join(receiver)
    msg['Cc'] = ', '.join(cc)
    msg['Subject'] = excel_file
    msg.attach(part)

    # Send mail
    tosend = receiver + cc
    smtp = SMTP_SSL('smtp.gmail.com')
    smtp.connect(smtp_server)
    smtp.login(mail_login, mail_passwd)
    smtp.sendmail(mail_login, tosend, msg.as_string())
    smtp.quit()
