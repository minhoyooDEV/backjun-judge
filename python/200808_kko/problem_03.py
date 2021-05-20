from collections import deque


def solution(n, k, cmd):
    data = deque([i for i in range(n)])
    # print('data', data)
    trash = deque()

    for c in cmd:
        splited = c.split()
        if len(splited) > 1:
            dir, x = splited[0], int(splited[1])
            if dir == "D":
                k += x
            elif dir == "U":
                k -= x
        else:
            dir = splited[0]
            if dir == "C":
                trash.append((k, data[k]))
                data.remove(data[k])
                if k == len(data):
                    k -= 1
            elif dir == "Z":
                oldK, oldX = trash.pop()
                if oldK <= k:
                    k += 1
                data.insert(oldK, oldX)

    sdata = set(data)
    result = ""
    for i in range(n):
        if i in sdata:
            result += 'O'
        else:
            result += 'X'
    return result


print(solution(8, 2, ["D 2", "C", "U 3", "C",
                      "D 4", "C", "U 2", "Z", "Z"]) == "OOOOXOOO")
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4",
                      "C", "U 2", "Z", "Z", "U 1", "C"]) == "OOXOXOOO")

# if __name__ == "__main__":
#     n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
#     n2, k2, cmd2 = 8, 2, ["D 2", "C", "U 3", "C",
#                           "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
#     print(solution(n, k, cmd))
#     print(solution(n2, k2, cmd2))
# 1
