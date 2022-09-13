import os

print("hello world from Python in testing limits")
print("The following is the ulimit from Python OS module")
stream = os.popen('ulimit -n')
output = stream.read()
print(output)
