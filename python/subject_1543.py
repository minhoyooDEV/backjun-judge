# 탐색

s = input()
w = input()

count = 0
i = 0
length = len(w)
while True:
    if s[i:length + i] == w:
        count += 1
        i += length
    else:
        i += 1

    if length + i > len(s):
        break

print(count)
