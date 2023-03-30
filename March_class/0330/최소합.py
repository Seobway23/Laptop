import sys
sys.stdin = open('input.txt', 'r')

# 최소합 재귀 구현
def DFS(i,j,sm):
    global min_sum
    # 1 종료조건
    if i > N-1 or j > N-1:
        return

    if sm > min_sum:
        return

    #print('sm:', sm)
    if i == N-1 and j == N-1:
        sm += arr[i][j]
        # print('sm:', sm)
        if sm < min_sum:
            min_sum = sm
        return

    DFS(i+1, j, sm + arr[i][j])
    DFS(i, j + 1, sm + arr[i][j])

# 각 칸은 오른쪽이나 아래로만 이동할 수 있음

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 13*N
    DFS(0,0,0)
    print(f"#{test_case} {min_sum}")
