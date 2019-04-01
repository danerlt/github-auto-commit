# coding: utf-8


from utils.func import get_github


def test_get_github():
    github = get_github()
    user = github.get_user()
    status = user.login()
    print(status)

