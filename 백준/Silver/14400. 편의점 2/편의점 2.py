# 기준이 되는 것은 결국 X, Y 좌표의 중간

N = int(input())
X_lst = [[0] for _ in range(N)]
Y_lst = [[0] for _ in range(N)]
arr = [[0, 0] for _ in range(N)]

for i in range(N):
    X, Y = map(int, input().split())
    X_lst[i], Y_lst[i] = X, Y
    arr[i] = [X, Y]

X_lst.sort()
Y_lst.sort()

iX, iY = X_lst[(N-1)//2], Y_lst[(N-1)//2]

ans = 0
for sx, sy in arr:
    ans += abs(sx - iX) + abs(sy-iY)

print(ans)