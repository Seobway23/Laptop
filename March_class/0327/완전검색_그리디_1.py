import sys
sys.stdin = open('input.txt', 'r')

def recur(cur, start, total):
    global min_total
    if cur == n - 1:
        min_total = min(min_total, arr[start][0] + total)
        return
    for i in range(1, n):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            recur(cur + 1, i, total + arr[start][i])
            visited[i] = 0


t = int(input())
for test_case in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_total = 100*n**2
    recur(0, 0, 0)
    print(f'#{test_case} {min_total}')