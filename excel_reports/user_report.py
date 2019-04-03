import openpyxl, pymysql, os
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

from excel_reports.excel_formatter.user_payments import user_payments_excel_maker
from settings.settings import host, user, passwd, db, port, smtp_server, mail_login, mail_passwd, receiver, cc

# Excel Settings
from excel_reports.requests.user_payments import user_payments_request

today = datetime.date.today().strftime('%d.%m.%Y')
excel_file = 'Oplata_polzovateley_' + today + '.xlsx'


def user_report():
    # Fetch Data from SQL server
    data = user_payments_request()

    # Write Data to Excel file
    user_payments_excel_maker(data)

    # Compose attachment
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

    # Wipe file
    os.remove(excel_file)
