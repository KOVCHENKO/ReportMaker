import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from datetime import datetime
from smtplib import SMTP_SSL

from settings.settings import mail_login, git_receiver, git_cc, smtp_server, mail_passwd


def send_mail():
    # Compose attachment
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("git_report/daily_report.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename("git_report/daily_report.txt"))

    # Compose message
    msg = MIMEMultipart()
    msg['From'] = mail_login
    msg['To'] = ', '.join(git_receiver)
    msg['Cc'] = ', '.join(git_cc)
    msg['Subject'] = 'Отчет по работе отдела за ' + str(datetime.today().strftime('%Y-%m-%d'))
    msg.attach(part)

    # Send mail
    tosend = git_receiver + git_cc
    smtp = SMTP_SSL('smtp.gmail.com')
    smtp.connect(smtp_server)
    smtp.login(mail_login, mail_passwd)
    smtp.sendmail(mail_login, tosend, msg.as_string())
    smtp.quit()
