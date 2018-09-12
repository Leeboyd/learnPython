'''
Pset-1 problem-3 試做失敗
不需要比較暫存字串，只要比較上一個字
比較成功後的row，比較目前長度
比較失敗下一個字串開始，重新計數
'''

alpha = 'abcdefghijklmnopqrstuvwxyz'
s = 'zgzapdgagwnvilfpaexyng'
tempSubstring = ''
tempSubstring2 = ''

for indI in range(len(s)):
    print('第', indI + 1, '輪始', tempSubstring, '挑戰者：', s[indI])
    indexOfTestingChar = alpha.find(s[indI])
    indexOfLastTestingChar =  alpha.find(s[indI - 1]) if indI - 1 >= 0 else 0 
    # alpha.find(s[indI - 1])
    indexOfLastTempSubstring = alpha.find(tempSubstring[-1]) if len(tempSubstring) >= 1 else 0
    # alpha.find(tempSubstring[-1])
    
    if (indI == 0 or len(tempSubstring) == 0):
      tempSubstring += s[indI]
    elif (indexOfTestingChar >= indexOfLastTestingChar and indexOfTestingChar >= indexOfLastTempSubstring and s[indI - 1] == tempSubstring[-1]): #indI - tempSubstring.find(tempSubstring[-1]) == 1
      tempSubstring += s[indI]
    elif (indexOfTestingChar >= indexOfLastTestingChar):
      if (len(tempSubstring2) > 0):
        tempSubstring2 =  tempSubstring2 + s[indI] if tempSubstring2.find(s[indI - 1]) != -1  and indexOfTestingChar >= alpha.find(tempSubstring2[-1])  else tempSubstring2
      else:
        tempSubstring2 = tempSubstring2.join([s[indI - 1], s[indI]])
        
      print('次列表', tempSubstring2)
      if (len(tempSubstring2) >= len(tempSubstring)):
        tempSubstring = tempSubstring2
        tempSubstring2 = ''
    elif (indexOfTestingChar < indexOfLastTestingChar and len(tempSubstring) == 1):
      tempSubstring = s[indI]
    print('第', indI + 1, '輪尾的 tempSubstring', tempSubstring)
    print('第', indI + 1, '輪尾的 tempSubstring2: ', tempSubstring2)
print('Longest substring in alphabetical order is: ',  tempSubstring)