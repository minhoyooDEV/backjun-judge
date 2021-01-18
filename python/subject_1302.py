case = int(input())

d = {}
for _ in range(case):
    name = input()
    if d.get(name) != None:
        d[name] += 1
    else:
        d[name] = 1

max_value = max(d.values())
print(list(filter(lambda d : d[1] == max_value, sorted(d.items())))[0][0])