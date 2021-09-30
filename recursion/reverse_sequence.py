import unittest
def reverse(seq, start, stop):
    '''reverse elements'''
    if start < stop-1:
        seq[start], seq[stop-1] = seq[stop-1], seq[start]
        reverse(seq, start+1, stop-1)
    return seq

class Test_reverse(unittest.TestCase):
    def test_reverse(self):
        our_seq = [1, 2, 3, 4, 5]
        reverse_seq = reverse(our_seq, 0, 5)
        self.assertEqual(reverse_seq, [5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()
