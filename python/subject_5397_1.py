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

  print(result)