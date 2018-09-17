def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    i = 1
    result = base
    if (exp == 0):
      return 1
    else:
      while i < exp:
        result =  result * base
        i += 1
      return result
