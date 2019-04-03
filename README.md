# github-auto-commit
github-auto-commit use PyGithub

看到[https://github.com/tywei90/git-auto-commit](https://github.com/tywei90/git-auto-commit)写了一个gihub自动提交的小工具，就想着使用Python来实现一个。

如何运行：
## 1.下载代码
```
git clone git@github.com:Lt-grint/github-auto-commit.git
```
## 2.github免密登录
针对上面两种克隆项目的方式，有两种免密登录设置,参考自[https://github.com/tywei90/git-auto-commit](https://github.com/tywei90/git-auto-commit)

### 2.1 生成公钥和私钥

检查本机的ssh密钥：
```bash
cd ~/.ssh
ls
```
如果提示：No such file or directory，说明你是第一次使用git，那就自己手动创建目录

使用ssh-keygen命令生成ssh密钥，命令如下：
```bash
ssh-keygen -t rsa
```
输入上面命令后，遇到选择直接回车，即可生成ssh 密钥。生成ssh 密钥后，可以到~/.ssh目录下查看相关文件，一般来说ssh 密钥会包含id_rsa和id_rsa.pub两个文件，分别表示生成的私钥和公钥。

### 2.2 拷贝公钥到你的github
在.ssh目录下，执行`cat id_rsa.pub`，复制所有公钥内容

点击github的头像，在下拉菜单中选择 setting 选项，在打开页面的左侧菜单中点击 SSH and GPG keys，然后点击新页面右上角绿色按钮 New SSH key。填写title值，并将复制的公钥内容粘贴到key输入框中提交。

### 2.3 测试链接github
我看网上是输入如下命令：
```bash
ssh –t git@github.com
```
然后，我的会报ssh: Could not resolve hostname \342\200\223t: Name or service not known的错误，搜了下，解决办法是执行下列命令：
```bash
ssh -t -p 22 git@github.com
```
-p表示修改服务器端口为22，当提示输入(yes/no)?时在后面输入yes回车即可。但是最后还是报错，后来又搜了下，执行如下代码：
```bash
ssh git@github.com
```
即将`-t`去掉就好了，看到 Hi ** You've successfully authenticated, but GitHub does not provide shell access. 说明连接成功了，大家可以都试一试。

## 3.配置授权
在`github-auto-commit/config`目录下有一个`auth.json`文件这个文件中配置了github的token和邮箱配置
```
{
  "github": {
    "access_token": "xxxxxxx",  # 这个是调用github API需要配置的token，建议配置这个
    "user": "xxxxxx",           # 这个是github 的用户名，
    "password": "xxx"           # 这个是github 的密码使用用户名密码
  },
  "sender": {                   # 发件人邮箱配置
    "host": "smtp.163.com",     # 邮箱SMTP地址
    "username": "xxxx",         # 邮箱用户名
    "password": "xxxx",         # 邮箱授权码，不是邮箱登录密码!!!
    "email": "xxxx@163.com"     # 邮箱账号
  },
  "receivers": [                # 收件人邮箱
    "test@163.com",
    "test@qq.com",
    "xxxx@163.com"
  ]
}
```

GitHub token配置如下图
![这里](http://static.zybuluo.com/danerlt/g7ev7kqprvyq1g75knvh5qpb/image_1d7ec1on41ecc110k1cgi150i1f5o9.png)
![TOKEN](http://static.zybuluo.com/danerlt/2kqlmr9389y2jdh3mgboil2m/image_1d7ec3oeq1fh2lq7p9v1kok136v16.png)

## 4.运行脚本：
```
cd github-auto-commit
python main.py
```

每天定时提交
```
cd github-auto-commit
python task.py
```
## 5.错误情况
如果发送邮件提示554错误，将发件人的邮箱添加到receivers即可解决