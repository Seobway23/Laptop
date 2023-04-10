import sys
sys.stdin = open('input.txt', 'r')

def DFS(index, sm, cnt):
    global ans

    if sm > K or N < cnt:
        return

    if index == n:
        if cnt == N and sm == K:
            ans += 1
        return


    DFS(index+1, sm + A[index], cnt + 1)
    DFS(index+1, sm, cnt)



A = [i for i in range(1,13)]
n = 12
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    DFS(0, 0, 0)
    print(f"#{test_case} {ans}")