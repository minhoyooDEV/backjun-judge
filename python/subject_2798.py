n, m = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))

# result = 0
# for a in range(len(l)):
#   for b in range(len(l)):
#     if a != b:
#       for c in range(len(l)):
#         if (c != a) and (c !=b):
#           local_sum = l[a] + l[b] + l[c]
#           if m >= local_sum and result <= local_sum:
#             result = local_sum
#           if local_sum == m:
#             break

# print(result)

result = 0
length = len(l)
for i in range(0,length):
  for j in range(i + 1,length):
    for k in range(j + 1,length):
      sum_value = l[i] + l[j] + l[k]
      if sum_value <= m:
        result = max(sum_value, result)

print(result)
