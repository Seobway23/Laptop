n = int(input())
ans = 0
while n >= 0:
    # 5의 배수니?
    if (n % 5) == 0:
        ans += (n // 5)
        print(ans)
        break
    n -= 3
    ans += 1

# n이 0보다 작을 때
else:
    print(-1)
