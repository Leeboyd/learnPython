s = "abcdefgh"
for index in range(len(s)):
  if s[index] == 'i' or s[index] == 'u':
    print("There is an i or u")

for char in s:
  if char == 'i' or char == 'h':
    print("There is an i or h")