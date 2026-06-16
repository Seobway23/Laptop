def solution(n):
    answer = 0
    l, r = 1, 1
    sm = 0
    
    # l이 끝날떄까지
    while l <= n:
        # n이 sm보다 작을 때
        if sm < n:
            if r <= n:
                sm += r
                r += 1
            # 범위 벗어나면 끝
            else:
                break
        # 같거나 클 때
        else:   
            if sm == n:
                answer += 1
            
            # left 줄이기
            sm -= l
            l += 1
            
    return answer