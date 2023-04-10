import sys
sys.stdin = open('input.txt', 'r')

def binary(i):
    global P
    if 0 < 2 * i <= N:
        if P[i] > P[2 * i]:
            P[i], P[i * 2] = P[i * 2], P[i]

        d = i
        ddd= P
        while 0 < d <= N:
            if P[d] < P[d//2]:
                P[d], P[d//2] = P[d//2], P[d]
            d = d//2





    if 0 < 2 * i + 1 <= N:
        if P[i] > P[2 * i + 1]:
            P[i], P[i * 2 + 1] = P[i * 2 + 1], P[i]

        dd = 2 * i + 1
        while 0 < dd <= N:
            if P[dd] < P[dd//2]:
                P[dd], P[dd//2] = P[dd//2], P[dd]
            dd = i//2


    if i == N:
        return
    else:
        i + 1




def sum_P(p):
    # 맨 뒷자리는 index(숫자 동일X)를 이용하거나 len으로 찾기 가능
    global P, cnt
    d = p//2
    dd = cnt

    if p//2 > 0:
        cnt += P[p//2]
        sum_P(p//2)

    else:
        return cnt

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0) # 원하는 인덱스에 자료 추가하는 방법 insert 이용
    i = 1 # 처음부터 시작
    binary(i) #이진트리 정렬
    cnt = 0
    sum_P(len(P)) #가장 마지막 노드(리스트의 맨 뒷자리)에서 부모 노드 찾아서 더하기
    last = 0

    print(f"#{test_case} {cnt}")
