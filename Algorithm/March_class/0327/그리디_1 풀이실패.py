import sys
sys.stdin = open('input.txt', 'r')

def func(i, j, k, cnt):
    global lst
    if cnt > min(lst):
        return

    if i >= k or j >= k:
        return

    cnt += arr[i][j]
    func(i+1, j, k, cnt)
    func(i, j+1, k, cnt)

    if i == k-1 and j == k-1:
        lst.append(( cnt ))
        return



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = [13*N]
    func(0, 0, N, 0)
    print(f'#{test_case} {min(lst)}')