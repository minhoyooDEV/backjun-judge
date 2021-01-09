import math
A, B, C = map(int, list(input().split(' ')))

if (C - B) <= 0:
    print(-1)
else:
  result = A / (C - B)
  is_float = bool(result % 1)
  result = math.ceil(result)
  if is_float:
    print(result)
  else:
    print (result + 1)
