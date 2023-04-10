import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [['1']*(N+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']*(N+2)]

    #초기값 설정
    queue = []
    visited = []
    ans = 0

    #시작 지점 찾기
    si, sj = 0, 0
    for i in range(1,N+1):
        for j in range(1, N+1):
            if arr[i][j] == '2':
                si, sj = i , j
                queue.append((si, sj))
                visited.append((si, sj))
                break

    # #미로 찾기 시작
    # ni, nj = si, sj
    while queue:
        # #종료 조건은 while문 만들면서 다시 쓰기
        #
        # #종료 조건 2
        # if (ni, nj) in visited and arr[ni][nj] != '0':
        #     ans = 0
        #     break

        #큐 원소 반환
        t = queue.pop()
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            if arr[t[0] + di][t[1] + dj] == '0' and not (t[0] + di, t[1] + dj) in visited:
                ni = t[0] + di
                nj = t[1] + dj
                queue.append((ni, nj))
                visited.append((ni, nj))

                # #종료 조건 1
                if arr[ni][nj] == '3':
                    ans = 1
                    break



    print(ans)





