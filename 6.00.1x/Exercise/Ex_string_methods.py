str1 = 'exterminate!'
str2 = 'number one - the larch'
print(str1.upper)                 # function
print(str1.upper())               # string, 'EXTERMINATE!'
print(str1.isupper())             # boolean, False
print(str1.islower())             # boolean, True
str2 = str2.capitalize()
print(str2)                       # string, 'Number one - the larch'
print(str2.swapcase())            # string, 'nUMBER ONE - THE LARCH'
print(str1.index('e'))            # int, 0
print(str2.index('n'))            # int, 8
print(str2.find('n'))             # int, 8
# print(str2.index('!'))            # error
print(str2.find('!'))             # int, -1
print(str1.count('e'))            # int, 3
str1 = str1.replace('e', '*')
print(str1)                       # string, '*xt*rminat*!'
print(str2.replace('one', 'seven'))# string, 'Number seven - the larch' 


