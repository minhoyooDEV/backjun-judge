from collections import defaultdict

N, M = map(int, input().split())


d = defaultdict(list)

for i, data in enumerate(map(int, input().split())):
    key = i + 1
    person = abs(data)
    d[person].append(key)

infect_num = int(input())


d2 = defaultdict(dict)

for key in d:
    data = d[key]
    for i in range(0, len(data), 2):
        d2[key][data[i]] = data[i+1]

infection_range = d2[infect_num]

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

            if (infection_start < start_time) and (start_time < infection_end) or (infection_start < end_time) and (end_time < infection_end) or (start_time < infection_start) and (infection_start < end_time) or (start_time < infection_end) and (infection_end < end_time):
                result.add(key)
                continue

for n in result:
    print(n, end=' ')
