from collections import deque

def solution(s):
    q = deque()
    
    for i in s:
        if i == "(":
            q.append(i)
        
        else:
            if len(q):
                q.pop()
            
            else:
                return False

    if len(q):
        return False
    else:
        return True