import pdb
"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

"""
def solution(N, A):
    B = [0] * N
    last = 0
    base = 0
    for x in A:
        if x >= 1 and x <= N:            
            B[x - 1] = max(base, B[x - 1]) + 1
            last = max(B[x - 1], last)
        elif x == N + 1:
            base = last
    for i in range(len(B)):
        B[i] = max(B[i], base)
    
    return B
"""

"""
def solution(n, arr):
    out = [0] * n
    m = 0
    last = 0
    for op in arr:
        op -= 1 
        if op == n:
            last = m
            continue
        out[op] = max(out[op], last) + 1
        m = max(m, out[op])
    for i in range(n):
        out[i] = max(out[i], last)
    return out
"""

N = 5
A = [3, 4, 4, 6, 1, 4, 4] # ans [3, 2, 2, 4, 2]

def solution(N, A):
    count = [0] * N
    base = 0    
    last = 0
    for i in range(len(A)):
        X = A[i]
        print(i, X, count, base, last)
        if X >= 1 and X <= N:        
            count[X - 1] = max(count[X - 1], base) + 1
            last = max(count[X - 1], base)
        elif X == N + 1:
            #pdb.set_trace()
            base = last
            
    for i in range(len(count)):
        count[i] = max(count[i], base)
            
    return count

print(solution(N, A))