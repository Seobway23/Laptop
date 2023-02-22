import sys
sys.stdin = open('input.txt', 'r')

def in_order(s):
    global lst, cnt
    d= cnt
    dd = lst

    if 0 < s <= N:
        #왼쪽 노드 시작
        in_order(s * 2)
        #인덱스 계산
        lst[s] = cnt
        cnt += 1
        #오른쪽 노드 시작
        in_order(s*2 + 1)




T = 10 #int(input())
for tc in range(1,T+1):
    dic = {}
    N = int(input())
    lst = [0]*(N+1)
    for _ in range(N):
        idx, Alpha, *hst = input().split()
        idx = int(idx)
        dic[idx] = Alpha


    cnt = 1
    in_order(1)
    ans = [''] * (N+1)
    for i in range(1, len(lst)):
        ans[lst[i]] = dic[i]

    print(f'#{tc}', end= ' ')
    print(*ans , sep= '')
