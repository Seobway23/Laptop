import sys
sys.stdin=open('input.txt', 'r')

def dfs(n,sm):
    global ans
    #가지치기는 제일 위해, 갱신가능성 0
    if ans<=sm:
        return

    #종료 시점에서 정답 처리
    if n == N:
        if ans > sm:
            ans = sm
        return

    #n+1의 하부함수 호출
    for j in range(N):
        if not v[j]:
            v[j] = 1            #방문 표시
            dfs(n+1, sm+arr[n][j])
            v[j] = 0            #사용 후 반드시 claer!


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ans=10*N
    v=[0]*N
    dfs(0, 0)

    print(f"#{test_case} {ans}")






