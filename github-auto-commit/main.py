#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from utils.func import git_commit, git_push, get_sender, get_receivers, send_email, get_github


def main():
    git_commit()
    git_push()
    commit_msg = os.popen("git log -1").read()
    sender = get_sender()
    receivers = get_receivers()
    send_email(**sender, receivers=receivers, title='git-auto-commit email', content=commit_msg)


if __name__ == '__main__':
    main()
