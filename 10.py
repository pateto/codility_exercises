import pdb
"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
"""

def solution(S):
    stack = []
    for C in S:
        print(C, stack)
        #pdb.set_trace()
        
        if C == '(':
            stack.append(C)
            
        if C == ')' and len(stack) == 0:
            return 0
            
        if C == ')' and stack[-1] == '(':
            stack.pop()           
    
    print(stack)
    if len(stack) > 0:
        return 0
    else:
        return 1
    
#S = "(()(())())"
#S = "())"
#S = "()(()()(((()())(()()))"
S = "()()()()()((()())(()()))"
print(solution(S))