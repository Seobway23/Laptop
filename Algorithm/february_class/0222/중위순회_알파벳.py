import sys
sys.stdin = open('input.txt', 'r')


visited = []
def in_order(i, c1, c2):
    a= visited
    #노드가 연결되어 있다면,

    # 왼쪽부터 다 읽으면
    if c1[i] != 0:
        visited.append(dic[i])
        in_order(c1[i], c1, c2)

    # 중앙 읽고
    if c1[i//2]:
        visited.append(dic[i//2])  # 부모 노드는 자식노드의 1/2

    # 오른쪽 읽고
    if c2[i] != 0:
        visited.append(dic[i])
        in_order(c2[i], c1, c2)

    # 그다음 return
    else:
        return

T = 1 #int(input())
for tc in range(1,T+1):
    N = int(input())
    dic = {} #알파벳 출력을 위해 dictionary 이용

    # 노드 연결
    c1 = [0] * (N + 1) #왼쪽
    c2 = [0] * (N + 1) #오른쪽
    for _ in range(N):
        idx, Alpha, *lst = input().split()
        idx = int(idx)
        dic[idx] =Alpha
        # lst에서 하나씩 꺼내서 연결해주기
        if len(lst) == 2:
            c1[idx] = int(lst[0])
            c2[idx] = int(lst[1])

        if len(lst) == 1:
            c1[idx] = int(lst[0])

    #시작 지점 파악
    start = 0
    for i in range(len(c1)-1, 0-1, -1):
        if c1[i] != 0:
            start = c1[i]
            break

    #visited 방문 기록
    #visited = []
   #함수 시작
    in_order(c1[start], c1, c2)


    print(f"#{tc} {visited}")







