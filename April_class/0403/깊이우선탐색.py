import sys
sys.stdin = open('input.txt', 'r')


def dfs(v, k): # 중복 빠짐 없이
    visited[v] = 1 # 중복 방지용
    ans.append(v) #ans 에 v 추가

    for w in adjL[v]:   # adj list에서 연결된 노드 확인
        if visited[w] == 0:  # 방문하지 않았다면, 재귀 호출
            dfs(w, k)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjL=[[] for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        adjL[i].append(j)
        adjL[j].append(i)

    visited = [0]*N
    ans = []
    dfs(1, V)
    print(f"#{test_case}", *ans)
