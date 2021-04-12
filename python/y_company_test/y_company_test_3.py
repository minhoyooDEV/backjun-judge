# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    checked = [0] * (len(A) + 1)

    count = 0

    for a in A:
        checked[a] = 1

        sum = 0

        for n in range(0, a):
            sum += checked[n]
        if sum == (a-1):
            count += 1

    return count

