n = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for stick in sticks:
    if n >= stick:
        cnt += 1
        n -= stick

    if n == 0:
        break

print(cnt)
