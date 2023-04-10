import sys
sys.stdin = open('input.txt', 'r')

'''
행을 기준으로 탐색하면 끝
'''

T=int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())
    arr= [[0]*(V+1) for _ in range(V+1)]

    #arr에 표시
    for _ in range(E):
        si, sj = map(int,input().split())
        arr[si][sj] = 1

    visited = []
    # 시작 위치 기록
    start = 1
    visited.append(start)

    #visited 기록 시작
    for i in range(V+1):
        for j in range(V+1):
            if not j in visited and arr[i][j] == 1:
                visited.append(j)

    print(f"#{test_case}", *visited)
