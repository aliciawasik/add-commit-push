import os

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print("")

print("Hello World!")
executeCommand("git status")
# executeCommand("git add -A")
# executeCommand("git commit -m 'Update files.'")
# execiteCommand("git push")