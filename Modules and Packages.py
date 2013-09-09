import re

# Your code goes here
ret = []
for x in dir(re):
    if "find" in x:
        ret.append(x)
print ret