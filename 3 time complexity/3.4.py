import time
start_time = time.time()

"""
Problem: You are given an integer n. Count the total of 1 + 2 + . . . + n.
"""

def slow_solution(n):
    ans = 0
    for i in range(n + 1):
        ans += i
    print(ans)
    
def solution(n):
    print(n*(n+1)/2)
    
#slow_solution(100000000)
"""
5000000050000000
--- 5.272220134735107 seconds ---
"""

solution(100000000)
"""
5000000050000000.0
--- 0.0 seconds ---
"""

print("--- %s seconds ---" % (time.time() - start_time))