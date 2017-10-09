import re
from sys import stdout
from random import randint, choice
from collections import defaultdict

with open('poetry.txt') as f:
    words = re.split(' +', f.read())

transition = defaultdict(list)
for w0, w1, w2 in zip(words[0:], words[1:], words[2:]):
    transition[w0, w1].append(w2)

i = randint(0, len(words)-3)
w0, w1, w2 = words[i:i+3]
for _ in range(500):
    stdout.write(w2+' ')
    w0, w1, w2 = w1, w2, choice(transition[w1, w2])