import os
commit_log = input("输入提交日志：")
os.system("git add .")
os.system('git commit -m "%s"' % commit_log)
os.system("git push")
os.system("mkdocs gh-deploy --force")
