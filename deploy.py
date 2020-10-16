import os
commit_log = input("输入提交日志：")
os.system("git commit -am %s" % commit_log)
os.system("git push")
os.system("mkdocs gh-deploy --force")
