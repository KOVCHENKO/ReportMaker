import os

from git import Repo, repo

empty_repo = Repo.init(os.path.join('emptyrepo', 'empty'))
origin = empty_repo.create_remote('origin', repo.remotes.origin.url)

print(origin)