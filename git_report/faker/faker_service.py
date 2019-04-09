# Make fake commit if there is no real
import json
from random import randint


# TODO: add real committing of this messages
def make_fake_commit(single_repo):
    commit_actions = json.load(open('./git_report/faker/faker.json'))

    # Record random commit info action
    random_action = randint(0, len(commit_actions) - 1)
    commit_random_action = commit_actions[random_action]["type"]

    # Record random commit info message
    random_message = randint(0, len(commit_actions[random_action]["messages"]) - 1)
    commit_random_message = commit_actions[random_action]["messages"][random_message]

    # Choose random module name
    random_commit_module = randint(0, len(single_repo['key_words']) - 1)
    commit_module_name = single_repo['key_words'][random_commit_module]

    return "%s (%s) %s" % (commit_random_action, commit_module_name, commit_random_message)
