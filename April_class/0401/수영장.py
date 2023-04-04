import sys
sys.stdin = open('input.txt', 'r')

def dfs(index, sm):
    global ans, lst
    #종료 조건
    if index > 11:
        if ans > sm:
            ans = sm
        return

    #하부 호춭
    #1일권
    dfs(index + 1, sm + n1*lst[index])
    #1달권
    dfs(index + 1, sm + n2)
    #3달권
    dfs(index + 3, sm + n3)
    #1년권
    dfs(index+ 12, n4)



T = int(input())
for test_case in range(1, T+1):
    n1, n2, n3, n4 = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 3000*12
    dfs(0,0)
    print(f"#{test_case} {ans}")