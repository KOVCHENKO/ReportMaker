import json

from git import Repo
from datetime import datetime, timedelta

from git_report.email_sender import send_mail


# Make report from different repos
from git_report.faker.faker_service import make_fake_commit


def git_report():
    repos = json.load(open('./git_report/repos.json'))

    f = open("git_report/daily_report.txt", "w")

    for single_repo in repos:
        get_repo_commits(single_repo, f)

    f.close()

    send_mail()


# Get commits for one day of single repo
def get_repo_commits(single_repo, f):
    is_there_commits = False

    # print(single_repo['name'])
    f.write(str(single_repo['name']))
    f.write(str("\n"))

    repo = Repo(single_repo['path'])

    commits = list(repo.iter_commits())

    for commit in commits:

        ts = int(commit.committed_date)
        commit_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')

        d = datetime.today() - timedelta(days=1)

        if commit_date == d.strftime("%Y-%m-%d"):
            is_there_commits = True
            # print(commit.author, commit.message)

            f.write(str(commit.message))

    f.write(str("\n"))

    if not is_there_commits:
        make_fake_commit(single_repo)
