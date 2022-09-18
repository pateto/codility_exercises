import pdb
"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
"""

"""
def remove_nest(S):
    
    if len(S) == 0:        
        return 1
        
    if len(S) == 2:
        if (S[0] == '{' and S[1] == '}') or (S[0] == '[' and S[1] == ']')or (S[0] == '(' and S[1] == ')'):
            return 1
            
    else:
    
        for i in range(len(S)-2):
            if (S[i] == '{' and S[i+1] == '}') or (S[i] == '[' and S[i+1] == ']')or (S[i] == '(' and S[i+1] == ')'):
            
                new_S = S[:i] + S[i+2:]
                
                return remove_nest(new_S)
                            
                break
            
    return 0
    
def solution(S):
    return remove_nest(S)
    
"""

def solution(S):


    #matches, stack = dict(['()', '[]', '{}']), []
    
    matches = {'(':')', '[':']', '{':'}'}
    stack = []

    for i in S:
        print(stack)
        if i in matches.values():
            if stack and matches[stack[-1]] == i:                
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    return int(not stack)



S = "{[(())[()]()]}"
#S = "{[()()]}"
#S  = "{[)()}"
#S = ")("
#S = "))(("
print(solution(S))