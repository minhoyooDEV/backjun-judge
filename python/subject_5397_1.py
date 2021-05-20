test_case = int(input())

output = ''
for _ in range(test_case):

  strs = list(input())
  result = ''
  cursur = 0
  for i in range(len(strs)):
    ch = strs[i]
    if len(result) == 0:
      if ch == '<' or ch =='>' or ch =='-':
        continue
      else:
        cursur +=1
        result = result + ch
    else:
      if ch == '<':
        if cursur > 0:
          cursur -= 1
        else:
          continue
      elif ch == '>':
        if cursur < len(result):
          cursur += 1
        else:
          continue
      elif ch == '-':
        target = list(result)
        target = target.pop(cursur - 1)
      else:
        if (cursur) == len(result):
          cursur +=1
          result += ch
        else:
          target = list(result)
          target = target[:cursur] + [ch] + target[cursur:]
          result = ''.join(target)


# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다. ↩