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

'''
Pset-2 problem-2
'''
alpha = 'abcdefghijklmnopqrstuvwxyz'
maxlength = 0
tempSubstring = ''
longestSubstring = ''

for indI in range(len(s)):
    # print('第', indI + 1, '輪始', tempSubstring, '挑戰者：', s[indI])
    indexOfTestingChar = alpha.find(s[indI])
    indexOfLastTestingChar =  alpha.find(s[indI - 1]) if indI - 1 >= 0 else 0 
    
    if (indI == 0 or len(tempSubstring) == 0):
        tempSubstring += s[indI]
        longestSubstring = tempSubstring
    else:
        if (indexOfTestingChar >= indexOfLastTestingChar):
            tempSubstring += s[indI]
            if (len(tempSubstring) > maxlength):
                longestSubstring = tempSubstring
                maxlength = len(longestSubstring)
        else:
            tempSubstring = s[indI]
    # print('第', indI + 1, '輪尾的 tempSubstring', tempSubstring)
print('Longest substring in alphabetical order is: ',  longestSubstring)