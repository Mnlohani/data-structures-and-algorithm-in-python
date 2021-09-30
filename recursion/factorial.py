import unittest

def factorial(n):
    ''' recursive function
    f(x) = n*(n-1)*....2*1'''
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
class TestFactorial(unittest.TestCase):
    
    def test_fact(self):
        self.assertEqual(factorial(5), 120)
    
    def test_fact_2(self):
        self.assertEqual(factorial(1), 1)
        
unittest.main(verbosity=2)