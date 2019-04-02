import json

from git import Repo
from datetime import datetime, timedelta

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


