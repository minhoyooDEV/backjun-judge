word = list(input())

d = {s: -1 for s in [chr(ch) for ch in range(ord('a'), ord('z') + 1)]}

for i in range(len(word)):
  ch = word[i]
  if (d.get(ch) == -1):
    d[ch] = i
print(' '.join([str(value) for key, value in d.items()]))