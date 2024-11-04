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

# Check if at least one argument is provided
commitMessage="Update files."
if len(sys.argv) > 2:
   commitMessage=sys.argv[2]

gitCommit="git commit -m \""+commitMessage+"\""


executeCommand(gitCommit)
executeCommand("git push")
