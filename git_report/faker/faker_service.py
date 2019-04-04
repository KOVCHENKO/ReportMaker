# Make fake commit if there is no real
def make_fake_commit(single_repo):
    commit_actions = [{
        "type": "feat",
        "messages": [
            "базовый фукнционал для работы",
            "еще функционал для работы",
        ]}, {
        "type": "fix",
        "messages": [
            "починил",
            "не починил"
        ]}, {
        "type": "docs",
        "messages": [
            "задокументировано",
            "не задокументировано"
        ]}, {
        "type": "refactor",
        "messages": [
            "отрефакторено",
            "не отрефакторено"
        ]}, {
        "type": "test",
        "messages": [
            "оттестировано",
            "не оттестировано"
        ]
    }]

    commit_modules = single_repo['key_words']

    random_commit_action = commit_actions[1]
    print(random_commit_action["type"])
    print(random_commit_action["messages"])

    for num, commit_action in enumerate(commit_actions):

        commit_action["type"] = "type"

        for commit_message in commit_action["messages"]:

            commit_message = 1


    # TODO: add real committing of this messages
    # print(commit_actions)

    # print(single_repo['key_words'])
