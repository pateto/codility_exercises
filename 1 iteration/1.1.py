"""
* * * * * * *
  * * * * *
    * * *
      *
"""

n = 4

"""
for i in range(n):
    for j in range(2*i):
        print(" ", end = '')
    for k in range(2*(n-i) - 1):
        print('* ', end = '')
    print()
"""

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end = '')
    for j in range(2 * i - 1):
        print('*', end = '')
    print()