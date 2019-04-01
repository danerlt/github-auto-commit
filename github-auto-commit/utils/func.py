# coding: utf-8

import json
from github import Github


def get_github():
    with open("../config/auth.json") as f:
        data = json.load(f)
        auth = data.get("access_token", None)
        user = data.get("user", None)
        password = data.get("password", None)
        try:
            g = Github(auth)
        except Exception as e:
            print(f"get by auth error:{e}")
        try:
            g = Github(user, password)
        except Exception as e1:
            print(f"get by user and password error:{e1}")
            raise Exception("your token or user and password is error, check your config")
        else:
            return g
