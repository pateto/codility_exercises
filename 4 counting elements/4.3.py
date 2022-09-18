import pdb
"""
Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 <= ai, bi <= m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them
"""

"""

A = [1, 2, 3, 4, 5]
B = [0, 11, 1, 1, 0]

    def swap_operation(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            tmp_A = A.copy()
            tmp_B = B.copy()
            tmp = tmp_A[i]
            tmp_A[i] = tmp_B[j]
            tmp_B[j] = tmp
            if sum(tmp_A) == sum(tmp_B):
                print(tmp_A, tmp_B, sum(tmp_A))
swap_operation(A, B)
"""

"""
def slow_solution(A, B):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                #return True
                print(i, j, sum_a)
            sum_a -= change
            sum_b += change

slow_solution(A, B)

"""

#A = [4, 1, 2, 1, 1, 2]
#B = [3, 6, 3, 3]
#m = 5

A = [5, 7, 4, 6]
B = [1, 2, 3, 8]
m = 10

def counting(A, m):    
    count = [0] * (m + 1)
    for i in A:
        count[i] += 1
    return count

def solution(A, B, m):
    sum_a = sum(A)
    sum_b = sum(B)
    d = abs(sum_a - sum_b)
    count_a = counting(A, m)
    print(sum_a, sum_b, d)
    #pdb.set_trace()
    for i in B:                
        if count_a[abs(i - d)] > 0:
            print(abs(i - d), i)
            return True
    return False
    
print(solution(A, B, m))
    