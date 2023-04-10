import sys
sys.stdin = open('input.txt', 'r')

def tree(n): #n은 시작 위치
    global N, last
    #종료 조건
    if last == N:
        return
    last += 1
    c = n #자식 노드
    p = c//2 #부모 노드
    while 0 < p and lst[p] > lst[c]:
        lst[p], lst[c] = lst[c], lst[p]
        #c, p 갱신
        c = p
        p = c//2

    #다음 차례 시작
    if n < N:
        tree(n+1)

def sum_p(i):
    cnt = 0
    p = i//2
    while 0 < p:
        cnt += lst[p]
        p = p//2

    return cnt

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.insert(0,0)
    last = 0 #last 카운트
    n = 1 #시작 위치 1
    tree(n)
    print(f"#{test_case} {sum_p(N)}")



