import sys
sys.stdin=open("input.txt", "r")

def dfs_stk(start):
    v = [0]*(V+1)
    stk = []
    s = start

    v[s] = 1
    alst.append(s)

    while True:
        # s에서 연결된, 미방문 노드 발견시 이동! (번호순)
        for e in range(1,V+1):
            if not v[e] and adj[s][e]:
                stk.append(s)       #주의: 되돌아올 위치(지금 기준점: 푸쉬)

                s = e
                v[s] = 1
                alst.append(s)
                break
                # 찾았으면 즉시, 그곳을 기준으로

        else: #더 이상 연결된 방문 노드 없는 경우
            if stk:
                s = stk.pop()       #스택에서 꺼낸 최근 기준점

            else:
                break



T=int(input())
for test_case in range(1, T+1):
    V,E=map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1

    alst=[]
    dfs_stk(1)
    print(f"#{test_case}", *alst)









    # V, E = map(int, input().split())
    # visited=[0]*V
    # #Link detecting
    # arr=list([0]*V for _ in range(V))
    # for _ in range(E):
    #     li, lj = map(int, input().split())
    #     arr[li][lj] = 1
    #     arr[lj][li] = 1
    #
    # stack=[]
    # i=1 #시작점 1
    # while True:
    #     for j in range(V):
    #         if arr[i][j]==1:
    #             stack.append(j)
    #             visited[j]=1
    #             break
    #
    #         else:
    #             B=stack.pop()
    #
    #
    #
    #     i+1
    #

