import termcolor
from termcolor import colored

infile = "/var/log/auth.log"

important = []
newimportant = []
keep_phrases = ["session"]

with open(infile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break
#variables to set of length of list
keep_phrases_length = len(keep_phrases)
important_length = len(important)

for x in range(0, important_length):
    for y in range(0,keep_phrases_length):
        red_string = colored(keep_phrases[y], 'red')
        new_string = important[x].replace(keep_phrases[y],red_string)
        newimportant.append(new_string)

for newimportant in newimportant:
    print (newimportant)
