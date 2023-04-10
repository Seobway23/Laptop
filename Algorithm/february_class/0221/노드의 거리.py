import sys
sys.stdin = open('input.txt', 'r')

def BFS(arr,S,G):
    #초기값 쓰기
    visited = [0] * (V+1) #0부터 V까지  개수 V+1
    queue = []

    #시잠점 큐, 방문 기록
    queue.append(S)
    visited[S] = 1

    #탐색 시작
    while queue:
        t = queue.pop(0)  #가장 앞에 있는 큐 빼내기
        for j in range(V+1):
            if arr[t][j] == 1 and visited[j] == 0: #노드가 있으면서 방문X의 경우
                queue.append(j)
                visited[j] = visited[t] + 1

            if visited[G] != 0: #들여쓰기 잘 할 것!!!!!!!
                return visited[G]-1  #도착 노드에 왔다면 cnt 출력

    return 0


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    arr = [ [0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        si, sj = map(int, input().split())
        arr[si][sj] = 1
        arr[sj][si] = 1

    S, G = map(int, input().split()) # S 출발노드, G 도착 노드

    print(f"#{test_case} {BFS(arr,S,G)}")



