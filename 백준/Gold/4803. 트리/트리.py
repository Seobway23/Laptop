import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

case_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 1) 그래프 초기화
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n+1)

    # 2) DFS로 사이클 여부 탐지
    def dfs(u, parent):
        visited[u] = True
        is_tree = True
        for v in adj[u]:
            if not visited[v]:
                # 재귀적으로 탐색
                if not dfs(v, u):
                    is_tree = False
            elif v != parent:
                # 이미 방문된 정점이면서 부모가 아니면 사이클
                is_tree = False
        return is_tree

    # 3) 모든 컴포넌트에 대해 트리인지 세기
    tree_count = 0
    for i in range(1, n+1):
        if not visited[i]:
            # 해당 컴포넌트가 사이클 없이 잘 연결돼 있으면 트리
            if dfs(i, 0):
                tree_count += 1

    # 4) 결과 출력
    if tree_count == 0:
        msg = "No trees."
    elif tree_count == 1:
        msg = "There is one tree."
    else:
        msg = f"A forest of {tree_count} trees."

    print(f"Case {case_num}: {msg}")
    case_num += 1
