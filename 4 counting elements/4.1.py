# Counting elements

A = [0, 0, 4, 2, 4, 5]
m = 10

def counting(A, m):    
    count = [0] * (m + 1)
    for i in A:
        count[i] += 1
    
    print(count)

counting(A, m)