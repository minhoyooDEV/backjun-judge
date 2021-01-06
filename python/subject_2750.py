arr = []
count = int(input())

for _input in range(count):
    arr.append(int(input()))

arr.sort()
for value in range(len(arr)):
    print(arr[value])