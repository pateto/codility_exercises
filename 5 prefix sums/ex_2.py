import pdb
"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

"""
def solution(A, B, K):
    count = 0    
    for i in range(A, B + 1):        
        if i%K == 0:
            count += 1
    return count
"""

"""
# solution from internet - Explanation: Number of integer in the range [1 .. X] that divisible by K is X/K. So, within the range [A .. B], the result is B/K - (A - 1)/K
"""

def solution(A, B, K):
    divisibles = 1
    if A == 0 and B == 0:
        return divisibles
    else:
        divisibles = B//K - (A - 1)//K
    return divisibles
 
assert solution(6, 11, 2) == 3
assert solution(0, 0, 11) == 1
assert solution(0, 14, 2) == 8
assert solution(1, 1, 11) == 0
assert solution(11, 13, 2) == 1
