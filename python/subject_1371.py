import sys

inputs = sys.stdin.read()

d = {}
for i in range(ord('a'), ord('z') + 1):
    d[chr(i)] = 0

max_num = 0
for i in range(len(inputs)):
  ch = inputs[i]
  if ch in d:
    d[ch] += 1
    if max_num < d[ch]:
       max_num = d[ch]

result = ''
for i in range(len(d.items())):
    if list(d.items())[i][1] == max_num:
        result += list(d.items())[i][0]

print(result)
