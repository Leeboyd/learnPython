cube = 8
guess = int(input('Cube is ' + str(cube) + '. Guess a number: '))

for guess in range(abs(cube) + 1): 
  if guess**3 > abs(cube):
    break
  if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
  else:
    print('Cube root of ' + str(cube) + ' is ' + str(guess))