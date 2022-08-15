import sys
import re
while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    else:
        S = re.sub('[a-zA-Z0-9\s]', '', s)[:-1]
        for i in range(len(S)//2+1):
            S = S.replace('()', '').replace('[]', '')
        print('yes' if len(S)==0 else 'no')