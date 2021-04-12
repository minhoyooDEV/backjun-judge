# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    data = defaultdict(list)

    for n in A:
        strNum = str(n)
        sum = 0
        for s in strNum:
            sum += int(s)

        data[sum].append(n)

    mx = -1
    for key in data:
        l = data[key]
        if len(l) >= 2:
            l.sort(reverse=True)
            sub_l = l[:2]
            sum = sub_l[0] + sub_l[1]
            if mx < sum:
                mx = sum

    return mx