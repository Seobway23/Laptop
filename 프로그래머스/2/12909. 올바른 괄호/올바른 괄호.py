from collections import deque
def solution(s):
    answer = True
    dq = deque()
    
    
    for i in s:
        if i == "(":
            dq.append(i)
        
        else:
            if dq:
                dq.pop()
            
            else:
                return False
            
    if dq:
        return False
    return True