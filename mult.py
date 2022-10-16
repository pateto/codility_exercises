from functools import reduce

def mult_1(a, b):
  ans = 0
  for i in range(a):
    ans += b
  return ans

def mult_2(a, b):
  return reduce(lambda x, y: x + y, [a for i in range(b)])

print(mult_1(3, 4))
print(mult_2(3, 4))