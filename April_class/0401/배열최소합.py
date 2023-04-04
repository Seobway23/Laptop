import sys
sys.stdin = open('input.txt', 'r')

'''
N*N 배열, 숫자를 골라 최소합, 세로로 같으 줄에서 두개 이상의 숫자를 고를 수 없음
조건에 맞게 숫자를 골랐을 때 최소 합 출력?

'''
def dfs(index,  sm):
    global ans, visited
    #종료 조건
    if index > N-1:
        return

    #print(index)
    #하부 호출
    for i in range(N):

        if visited[i] == 0:
            visited[i] = 1
            sm += arr[index][i]
            if ans > sm:
                if index == N-1:
                    ans = sm

                else:
                    dfs(index + 1, sm)

            visited[i] = 0
            sm -= arr[index][i]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 9 * N
    dfs(0,0)
    print(f"#{test_case} {ans}")