# @tag qsort, quicksort, 퀵정렬

count = int(input())

nums = list(map(lambda n: int(input()), range(count)))

def q_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    prev_arr, equal_arr, next_arr = [], [], []

    for num in arr:
        if num < pivot:
            prev_arr.append(num)
        elif num > pivot:
            next_arr.append(num)
        else:
            equal_arr.append(num)

    return q_sort(prev_arr) + equal_arr + q_sort(next_arr)

print(q_sort(nums))
