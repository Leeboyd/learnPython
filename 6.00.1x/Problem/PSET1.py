'''
Pset-1 problem-1
'''
vowels = 'aeiou'
countOfVowels = 0

for char in s:
  if (char in vowels):
    countOfVowels+=1
print('Number of vowels: ' + str(countOfVowels))