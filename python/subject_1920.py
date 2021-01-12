count_n = int(input())
# d = {n for n in list(map(int, input().split(' ')))}
d = set(map(int, input().split(' ')))
count_m = int(input())
nums = list(map(int, input().split(' ')))

for i in nums:
    if i in d:
        print(1)
    else:
        print(0)
