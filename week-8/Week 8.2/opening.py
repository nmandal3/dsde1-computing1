import os

os.chdir('C:/Users/nmand/Documents/Computing1/dsde1-computing1/week-8/Week 8.2/text-files')
with open('mercutio.txt') as f:
    #text = f.read
    lines = f.readlines()
i = 0
while i < 10:
    print(lines[i])
    i += 1