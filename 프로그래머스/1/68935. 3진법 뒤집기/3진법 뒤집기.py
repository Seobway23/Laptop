def solution(n):
    answer = 0
    
    ans = three(n)
    print(ans)
    
    
    thr = 1
    for  i in range(len(ans) -1, -1, -1):
        answer += thr * int(ans[i])
        thr *= 3
    
    return answer


def three(n):
    ans = ''
    while True:
        if n == 0:
            return ans
        
        ans += str(n % 3)
        n = n // 3
        
        