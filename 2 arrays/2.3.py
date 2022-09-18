import pdb
"""
Problem: Given array A consisting of N integers, return the reversed array.
Solution: We can iterate over the first half of the array and exchange the elements with
those in the second part of the array
"""

A = [10,9,8,7,6,5,4,3,2,1,0]

def reverse(A):
    N = len(A)
    #pdb.set_trace()
    for i in range(N//2):
        k = N - i - 1
        print(i, k)
        A[i], A[k] = A[k], A[i]
        
    print(A)

reverse(A)