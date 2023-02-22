import sys
sys.stdin = open('input.txt', 'r')

def tree(N):
    global c1, c2, cnt, visited
    #왼쪽 cnt
    if c1[N] !=0:
        visited.append(c1[N])
        cnt += 1
        tree(c1[N])

    # 오른쪽 cnt
    if c2[N] != 0:
        visited.append(c2[N])
        cnt += 1
        tree(c2[N])

    return


T= int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    n = 15

    c1 = [0] * (n + 1)
    c2 = [0] * (n + 1)
    #노드 저장
    lst = list(map(int, input().split()))
    for i in range(0, len(lst),2):
        # 부모노드lst[i], 자식노드 lst[i+1]
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i+1]

        else:
            c2[lst[i]] = lst[i + 1]
    #처음 위치 visited 저장
    visited = []
    visited.append(N)
    #처음위치 cnt
    cnt = 1

    #함수 동작
    tree(N)

    print(f'#{tc} {cnt}')


