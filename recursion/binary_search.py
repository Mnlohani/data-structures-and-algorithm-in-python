def binary_search(seq, target, low, high):
    
    mid = (low + high) // 2
    if low > high:
        return False 
    else:
        if target == seq[mid]:
            return "the target number found at "+ str(mid+1) + ' position'
        elif target < seq[mid]:
            return binary_search(seq, target, low, mid - 1)
        else:
            return binary_search(seq, target, mid + 1, high)

if __name__ == '__main__':
    sequence = [5, 8, 9, 10, 19]
    output = binary_search(sequence, 11, 0, len(sequence)-1)
    print(output)
