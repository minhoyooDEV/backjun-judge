char = input()

code = ord(char)
if (ord('0') <= code and ord('9') >= code) or (ord('a') <= code and ord('z') >= code) or (ord('A') <= code and ord('Z') >= code):
  print(code)