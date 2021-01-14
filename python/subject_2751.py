# @tag qsort, quicksort, 퀵정렬
import sys

count = int(input())

nums = list(map(lambda n: int(sys.stdin.readline().rstrip()), range(count)))


def merge(left, right):
    merged = []
    l_point, r_point = 0, 0

    while len(left) > l_point and len(right) > r_point:
        if left[l_point] > right[r_point]:
            merged.append(right[r_point])
            r_point += 1
        else:
            merged.append(left[l_point])
            l_point += 1
    while len(left) > l_point:
        merged.append(left[l_point])
        l_point += 1
    while len(right) > r_point:
        merged.append(right[r_point])
        r_point += 1

    return merged


def merges_split(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = merges_split(data[:medium])
    right = merges_split(data[medium:])
    return merge(left, right)


for n in merges_split(nums):
    print(n)
