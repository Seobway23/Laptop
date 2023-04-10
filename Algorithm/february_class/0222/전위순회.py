import sys
sys.stdin = open('input.txt', 'r')

def tree(i, c1, c2):
    #부모 노드와 연결되어 있다면,
    # c1은 왼쪽 노드
    if c1[i] != 0: #1 c1이 0이 아니라면, vistied에 추가
        visited.append(c1[i])
        tree(c1[i], c1, c2)
    # c2는 오른쪽 노드
    if c2[i] !=0: #1이 다 끝나고 c2가 0이 아니라면 visited에 추가
        visited.append(c2[i])
        tree(c2[i], c1, c2)

    else:
        return


T = int(input())
for tc in range(1,T+1):
    N= int(input())
    lst = list(map(int, input().split()))
    c1 = [0] * (N + 1) # 왼쪽 노드
    c2 = [0] * (N + 1) # 오른쪽 노드

    #부모, 자식 노드 기록
    for i in range(0 , len(lst), 2):
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i+1]

        else: #c1이 0이 아니라면 -> 이진트리에서만 가능
            c2[lst[i]] = lst[i+1]

    #처음 시작지점 기록
    start = 0
    for i in range(len(c1)):
        if c1[i] !=0:
            start = i
            break
    for i in range(1, start): #그럴 일이 없음 ㅋㅋ
        if c2[i] < start :
            start = i
            break
    #visited 리스트, 시작점 리스트 추가
    visited = []
    visited.append(start)

    #함수 실행
    tree(start, c1, c2)

    print(f"#{tc}", *visited)



