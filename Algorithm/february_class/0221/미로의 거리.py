import sys
sys.stdin = open('input.txt', 'r')

def BFS(arr, S):
    visited = [['0']*(N+2) for _ in range(N+2)]
    queue = []
    queue.append(S)
    ni, nj = 0, 0
    ans = 0

    # 탐색 시작
    while queue:
        t = queue.pop(0)

        #방문 표시
        if visited[t[0]][t[1]] == '0':
            visited[t[0]][t[1]] = '1'

        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
            if arr[t[0] + di][t[1] + dj] == '3': #만약에 3을 찾으면 ans = 1그리고 반환
                ans = int(visited[t[0]][t[1]]) -1 # 처음 1로 시작했기 때문에 1을 빼줘야 한다.
                return ans

            if arr[t[0] + di][t[1] + dj] == '0' and visited[t[0] + di][t[1] + dj] == '0': #arr가 0이면서 방문하지 않았다면,
                ni = t[0] + di
                nj = t[1] + dj
                queue.append((ni, nj))
                visited[ni][nj] = str(int(visited[t[0]][t[1]]) + 1)

    # 다 돌았는데 3을 못찾았으면, return 0
    return 0






    return

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [['1']*(N+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']*(N+2)]

    #시작 지점 찾기
    for i in range(1,N+1):
        for j in range(1, N + 1):
            if arr[i][j] == '2':
                S = (i, j)
                break


    print(f"#{test_case} {BFS(arr, S)}")