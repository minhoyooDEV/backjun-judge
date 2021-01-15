nums = list(map(int, input()))

def merge(left, right):
    result = []
    l_point, r_point = 0, 0
    while len(left) > l_point and len(right) > r_point:
        if left[l_point] > right[r_point]:
            result.append(left[l_point])
            l_point += 1
        else:
            result.append(right[r_point])
            r_point += 1
    while len(left) > l_point:
        result.append(left[l_point])
        l_point += 1
    while len(right) > r_point:
        result.append(right[r_point])
        r_point += 1

    return result


def merge_split(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_split(arr[mid:])
    right = merge_split(arr[:mid])
    return merge(left, right)


print(''.join(map(str,(merge_split(nums))))
)