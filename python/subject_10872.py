def fact(n):
  if n <= 1:
    return n
  return n * fact(n - 1)

n = int(input())

if n == 0 :
  print(1)
elif n == 1:
  print(1)
else:
  print(fact(n))
