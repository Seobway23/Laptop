import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
A = list(map(int, input().split()))

start = 1; end = max(A);
while start <= end:
    cnt = 0
    mid = (start+end)//2

    for i in A:
        if i- mid > 0:
            cnt += i - mid

    if cnt >= M:
        start = mid + 1

    else:
        end = mid - 1

print(end)