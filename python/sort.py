
def quicksort(data_list):
    if len(data_list) <= 1:
        return data_list
    else:
        pivot = data_list[0]

        left = [item for item in data_list[1:] if pivot > item]
        right = [item for item in data_list[1:] if pivot <= item]

        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([50,90,1,14,8,21,65]))