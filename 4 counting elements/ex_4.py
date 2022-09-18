"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

A = [1, 3, 6, 4, 1, 2]
#A = [1, 2, 3]
#A = [-1, -3]
#A = [2]

def solution(A):
    # count elements
    n = len(A)
    count = [0] * n
    for i in A:
        if i > 0 and i <= n and count[i - 1] == 0:
            count[i - 1] += 1
    
    # find min value
    if sum(count) == n:
        return n + 1
    else:
        for i in range(len(count)):
            if count[i] == 0:
                return i + 1
    
print(solution(A))