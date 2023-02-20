import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    q = []
    ans = 0
    for i in range(1, N+1):
        q.append((i, lst.pop(0)))


    while q:
        n, piz = q.pop(0)
        piz = piz // 2
        if piz == 0:
            if lst:
                i += 1
                q.append((i, lst.pop(0)))

        else:
            q.append((n, piz))

    ans = n


    print(f"#{test_case} {ans}")