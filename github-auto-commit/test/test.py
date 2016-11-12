# coding: utf-8

import os
from datetime import datetime
import unittest
from utils.func import get_github, get_sender, get_receivers, send_email


class GithubTestCase(unittest.TestCase):
    def setUp(self):
        self.github = get_github()

    def test_get_user(self):
        user = self.github.get_user()
        self.assertIsNotNone(user)

    def test_login(self):
        user = self.github.get_user()
        login_value = user.login
        self.assertIsNotNone(login_value)

    def test_get_repo(self):
        username = 'Lt-grint'
        reponame = 'github-auto-commit'
        repo = self.github.get_repo(f'{username}/{reponame}')
        self.assertEqual(repo.name, reponame)

    def test_commit(self):
        test_file = 'text.txt'
        with open(test_file, 'a+') as f:
            date = datetime.now()
            content = date.strftime('%Y-%m-%d %I:%M:%S %p')
            f.write(content)
            os.system("git add text.txt")
            comment = f'update text.txt append {content}'
            os.system(f'git commit -m "{comment}"')

    def test_send_mail(self):
        sender = get_sender()
        receivers = get_receivers()
        send_email(**sender, receivers=receivers, title='test email', content='hahahah')


if __name__ == '__main__':
    unittest.main()
