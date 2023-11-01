from collections import deque

def create_net(cpts, cnns):
    # 딕셔너리
    graph = { i : [] for i in range(1, cpts + 1)}

    for cnn in cnns:
        # 양방향 연결 필요함!!!
        graph[cnn[0]].append(cnn[1])
        graph[cnn[1]].append(cnn[0])

    return graph


def ans(graph):
    global cpts
    # BFS
    visited = [0] * (len(graph) + 1)
    visited[1] = 1
    q = deque([1])

    while q:
        cpt = q.popleft()
        for cnn_cpt in graph[cpt]:
            # 미방문 이면 추가
            if not visited[cnn_cpt]:
                visited[cnn_cpt] = 1
                q.append(cnn_cpt)


    return sum(visited) - 1


cpts = int(input())
cnn_num = int(input())
cnns = [list(map(int, input().split())) for _ in range(cnn_num)]
graph = create_net(cpts, cnns)


print(ans(graph))