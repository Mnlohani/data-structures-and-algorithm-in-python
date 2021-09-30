def binary_sum(seq, start, stop):
    '''sum of sequence in binary recursion
    stop is not included'''
    
    if start >= stop:         #zero element
        return 0
    elif start == stop - 1:     #one element
        return seq[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(seq, start, mid) + binary_sum(seq, mid, stop)

print(binary_sum([10,20,30,40], 2, 4))