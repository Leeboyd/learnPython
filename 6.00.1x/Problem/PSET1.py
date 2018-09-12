'''
Pset-1 problem-1
'''
vowels = 'aeiou'
countOfVowels = 0

for char in s:
  if (char in vowels):
    countOfVowels+=1
print('Number of vowels: ' + str(countOfVowels))

'''
Pset-2 problem-2
'''
# s = 'obobbobbobobbobobubobobbobobocrobobbobobo'
keyword = 'bob'
keywordOccurs = 0

for index in xrange(len(s)):
  stringTobeCheck = s[index:index+3]
  if (len(stringTobeCheck) < 3):
    break
  if (s[index:index+3] == keyword):
    keywordOccurs += 1
  
print('Number of times bob occurs is: ' + str(keywordOccurs))