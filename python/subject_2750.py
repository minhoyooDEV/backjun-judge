arr = []
count = int(input())

for _input in range(count):
    arr.append(int(input()))

arr.sort()
for value in range(len(arr)):
    print(arr[value])

    # @tag qsort, quicksort, 퀵정렬
# import sys

# count = int(sys.stdin.readline())

# nums = []
# for _ in range(count):
#     nums.append(int(sys.stdin.readline()))


# def q_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     prev_arr, equal_arr, next_arr = [], [], []

#     for num in arr:
#         if num < pivot:
#             prev_arr.append(num)
#         elif num > pivot:
#             next_arr.append(num)
#         else:
#             equal_arr.append(num)

#     return q_sort(prev_arr) + equal_arr + q_sort(next_arr)


# for n in q_sort(nums):
#     print(n)
