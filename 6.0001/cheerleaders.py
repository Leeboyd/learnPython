legal_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
    char = word[i]
    if char in legal_letters:
      print("Give me a/an " + char + "! " + char)
    else:
      print("Give me a/an " + char + "! " + char)
    i += 1
print("What dose that spell?")
for i in range(times):
  print(word.upper() + "! ")