import sys
sys.stdin = open('input.txt', 'r')

def DFS(i, sm):
    global cnt, lst
    if i == N-1:
        if sm == K:
            cnt += 1
        return

    DFS(i+1, sm)
    DFS(i+1, sm + lst[i])



T=int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    #0부터 재귀해야 하기 때문에 -1로 둠
    DFS(-1, 0)
    print(f"#{test_case} {cnt}")