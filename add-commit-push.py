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
if len(sys.argv) > 1:
    # Print the first argument (index 1, since index 0 is the script name)
    print(f"First argument: {sys.argv[1]}")
    print(f"Second argument: {sys.argv[2]}")
else:
    print("No arguments provided.")

gitCommit="git commit -m \"Update files.\""
executeCommand(gitCommit)
executeCommand("git push")