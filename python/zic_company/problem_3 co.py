from collections import defaultdict

N, M = [6, 144]
# N, M = map(int, input().split)

infect_num = 1
d = defaultdict(list)


# for i, data in enumerate(range(1, M + 1)):
for i, data in enumerate(map(int, "2 1 3 4 -3 -4 -1 -2 5 -5 1 6 -1 -6".split())):
    key = i + 1
    person = abs(data)
    d[person].append(key)


d2 = defaultdict(dict)

for key in d:
    data = d[key]
    for i in range(0, len(data), 2):
        d2[key][data[i]] = data[i+1]

infection_range = d2[infect_num]
print(infection_range)

result = set()

for key in d2:
    if key == infect_num:
        continue
    target_person = d2[key]

    for start_time in target_person:
        end_time = target_person[start_time]

        for start in infection_range:
            infection_start = start
            infection_end = infection_range[infection_start]

            if (infection_start < start_time) and (start_time < infection_end) or (infection_start < end_time) and (end_time < infection_end) or (start_time < infection_start) and (infection_start < end_time) or (start_time < infection_end) and (yy < end_time):
                result.add(key)
                continue

print(result)
