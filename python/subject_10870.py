def fibo(n):
  if n <= 1:
    return n
  return fibo(n - 1) + fibo(n - 2)

n = int(input())

if n == 0 :
  print(0)
elif n == 1:
  print(1)
else:
  print(fibo(n))
