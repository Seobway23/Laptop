s = int(input())
sm, cnt = 0, 0

while sm <= s:
    cnt += 1
    sm += cnt

print(cnt - 1)