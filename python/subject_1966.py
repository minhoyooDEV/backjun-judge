case_size = int(input())

for _ in range(case_size):
  n, m = list(map(int, input().split(' ')))
  queue = list(map(int, input().split(' ')))
  queue = [(i, idx) for idx, i in enumerate(queue)] #중요도, 초기인덱스

  count = 0

  while True:

    #max(queue, key=lambda x: x[0]) 특정 조건중 가장 큰 값을 출력
    if queue[0][0] == max(queue, key=lambda x: x[0])[0]: #큐의 가장 앞에있는 데이터의 중요도가 가장 큰지 확인한다.
      count += 1 #로직을 수행하니 count 증가
      if queue[0][1] == m: #제일 앞에 있는 데이터가 찾고있는 데이터라면
        print(count) #프린트하고
        break # 멈춘다
      else:
        queue.pop() #중요도가 같은상황
    else: #아니라면
      queue.append(queue.pop()) #뒤로보냄
