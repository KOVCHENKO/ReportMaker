import datetime
import os

from excel_reports.email_sender import send_mail
from excel_reports.excel_formatter.user_payments import user_payments_excel_maker

# Excel Settings
from excel_reports.requests.user_payments import user_payments_request

today = datetime.date.today().strftime('%d.%m.%Y')
excel_file = 'Oplata_polzovateley_' + today + '.xlsx'


def user_report():
    # Fetch Data from SQL server
    data = user_payments_request()

    # Write Data to Excel file
    user_payments_excel_maker(data)

    # Send mail
    send_mail()

    # Wipe file
    os.remove(excel_file)
