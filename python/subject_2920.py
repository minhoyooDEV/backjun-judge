l = list(map(int, input().split(' ')))

ascending = True
descending = True
for index in range(1, len(l)):
    if l[index - 1] > l[index]:
      ascending = False
    elif l[index - 1] < l[index]:
      descending = False

    if not (ascending or descending):
      break

if ascending:
  print('ascending')
elif descending:
  print('descending')
else:
  print('mixed')


