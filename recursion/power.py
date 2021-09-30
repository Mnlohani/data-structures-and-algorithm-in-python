import unittest
def power(x, n):
    '''power of x to n'''
    if n==0:
       return 1 
    else:
        return x * power(x, n-1)
        

print(power(2,5))