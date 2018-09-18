def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    a = abs(a)
    b = abs(b)
    
    if (b > a):
      temp = a
      a = b
      b = temp
    
    while True:
      a %= b
      if a == 0:
        return b
      b %= a
      if b == 0:
        return a
