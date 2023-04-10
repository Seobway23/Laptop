import sys
sys.stdin = open('input.txt', 'r')


def bfs(visited):
    global node_lst
    # q 추가
    q = []
    visited = [1]
    q.append(1)
    while q:
        t = q.pop(0)
        # g = []
        # for i in node_lst[t]:
        #     if i not in visited:
        #         g.append(i)
        #item = min(g)
        # if item not in visited:
        #     q.append(item)
        #     visited.append(item)

        # 노드 연결이면서 미방문이면 q,v추가
        for i in node_lst[t]:
            if i not in visited:
                q.append(i)
                visited.append(i)

    return visited


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    node_lst = [[] for _ in range(V+1)]
    visited = []
    for _ in range(E):
        n1, n2 = map(int,input().split())
        node_lst[n1].append(n2)
        node_lst[n2].append(n1) # 방향이 없으면 추가

    ans = bfs(visited)
    print(f"#{test_case}", *ans)
