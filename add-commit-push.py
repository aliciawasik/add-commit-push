import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)

print("Hello World!")