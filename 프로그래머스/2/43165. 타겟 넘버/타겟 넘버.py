# i: 현재 인덱스 위치, sm : 합,  target ?
def dfs(i, sm, target, numbers):
    global ans
    if i == len(numbers):
        if sm == target: 
            ans+= 1
        
        return 
    
    # 더하기
    dfs(i + 1, sm + numbers[i], target, numbers)
    
    # 빼기
    dfs(i + 1, sm - numbers[i], target, numbers)
        
ans = 0
def solution(numbers, target):
    
    # dfs 돌리고 n 이 len(numbers)와 같다면 return
    dfs(0, 0, target, numbers)
    return ans