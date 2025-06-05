import os
import subprocess
import pickle

# 1. Command Injection
user_input = input("Enter something to run: ")
os.system("echo " + user_input)

# 2. Subprocess injection
subprocess.run("ls " + user_input, shell=True)
  
# 3. Unsafe deserialization
data = b"cos\nsystem\n(S'echo vulnerable'\ntR."
pickle.loads(data)
#end
