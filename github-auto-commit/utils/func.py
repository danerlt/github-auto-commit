# coding: utf-8

import os
import json
import smtplib
from github import Github
from datetime import datetime
from email.mime.text import MIMEText


def get_config(file="../config/auth.json"):
    if os.path.isfile(file):
        with open(file, "r") as f:
            data = json.load(f)
            return data


def get_github():
    try:
        data = get_config()
        github = data.get("github")
        auth = github.get("access_token", None)
        g = Github(auth)
    except Exception as e:
        print(f"get by auth error:{e}")
        raise Exception("your token error, check your config")
    else:
        return g


def get_github_by_user_pass():
    try:
        data = get_config()
        github = data.get("github")
        user = github.get("user", None)
        password = github.get("password", None)
        g = Github(user, password)
    except Exception as e:
        print(f"get by user and password error:{e}")
        raise Exception("your user and password is error, check your config")
    else:
        return g


def get_sender():
    try:
        data = get_config()
        sender = data.get("sender")
    except Exception as e:
        print(f"get by user and password error:{e}")
        raise Exception("your user and password is error, check your config")
    else:
        return sender


def get_receivers():
    try:
        data = get_config()
        receivers = data.get("receivers")
    except Exception as e:
        print(f"get by user and password error:{e}")
        raise Exception("your user and password is error, check your config")
    else:
        return receivers


def send_email(host=None, username=None, password=None, email='', receivers=[], title='', content=''):
    """发送邮件

    :param host: SMTP服务器
    :param username: 用户名
    :param password: 授权密码，非登录密码
    :param email: 发件人邮箱(最好写全, 不然会失败)
    :param receivers: 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    :param title: 邮件主题
    :param content: 邮件内容
    :return:
    """
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(email)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(username, password)  # 登录验证
        smtpObj.sendmail(email, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def git_commit_and_push(file='text.txt'):
    with open(file, 'a+') as f:
        date = datetime.now()
        content = date.strftime('%Y-%m-%d %I:%M:%S %p')
        f.write(content)
        os.system(f"git add {file}")
        comment = f'update text.txt append {content}'
        os.system(f'git commit -m "{comment}"')
        os.system('git push origin master')
