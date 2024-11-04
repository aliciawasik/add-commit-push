import os
import sys

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print("")

print("AddCommitPush")
print("")
executeCommand("git status")

response=input("Would you like to AddCommitPush (y/n)? ")

# Check if the input is not equal to "y"
if response != "y":
    sys.exit()

executeCommand("git add -A")
executeCommand("git commit -m \"Update code.\"")
executeCommand("git push")