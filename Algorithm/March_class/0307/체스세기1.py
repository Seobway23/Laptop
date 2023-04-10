import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
ans = n*m

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        draw1 = 0
        draw2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 모두 짝수 일 경우
                    if arr[a][b] != 'B':
                        draw1 += 1
                    if arr[a][b] != 'W':
                        draw2 += 1
                else: #나머지인 경우
                    if arr[a][b] != 'W':
                        draw1 += 1
                    if arr[a][b] != 'B':
                        draw2 += 1

print(ans)

