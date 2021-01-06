case_size = int(input())

for _ in range(case_size):
  n, m = list(map(int, input().split(' ')))
  queue = list(map(int, input().split(' ')))

  print_count = 0
  while len(queue) > 0:
    print_count += 1
    for i in range(len(queue)):
      if queue[0] < queue[i]:
        queue.append([0])
        del queue[0]



