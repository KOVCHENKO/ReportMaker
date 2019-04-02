import json
import os
from email import encoders
from email.mime.base import MIMEBase

from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from git import Repo
from datetime import datetime, timedelta

from settings import mail_login, git_receiver, git_cc, smtp_server, mail_passwd


def main():

    repos = json.load(open('./git_report/repos.json'))

    f = open("git_report.txt", "w")

    for single_repo in repos:

        print(single_repo['name'])
        f.write(str(single_repo['name']))
        f.write(str("\n"))

        repo = Repo(single_repo['path'])
        now = datetime.now()

        commits = list(repo.iter_commits())

        for commit in commits:

            ts = int(commit.committed_date)
            commit_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
            today = now.strftime("%Y-%m-%d")

            d = datetime.today() - timedelta(days=1)

            if commit_date == d.strftime("%Y-%m-%d"):
                print(commit.author, commit.message)

                f.write(str(commit.message))

        f.write(str("\n"))

    f.close()

    # Compose attachment
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("git_report.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename("git_report.txt"))

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

if __name__ == '__main__':
    main()

