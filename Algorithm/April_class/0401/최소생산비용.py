import sys
sys.stdin = open('input.txt', 'r')

'''
A사 N 종의 N 곳의 공장에 한곳당 한가지 씩만 생산 -> 인덱스 중복 허용 X
'''

def dfs(index, sm):
    global ans

    if sm > ans:
        return

    # 하부 함수 호출
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            sm += arr[index][i]

            if index == N-1:
                if ans > sm:
                    ans = sm

            else:
                dfs(index+1, sm)
            visited[i] = 0
            sm -= arr[index][i]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    visited = [0]*N
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * N
    dfs(0, 0)
    print(f"#{test_case} {ans}")