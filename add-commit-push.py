import os

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print("")

print("AddCommitPush")
print("")
executeCommand("git status")
executeCommand("git add -A")
executeCommand("git commit -m \"Update code.\"")
executeCommand("git push")