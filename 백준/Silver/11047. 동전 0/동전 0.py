n, score = map(int, input().split())
lst = list(int(input()) for _ in range(n))

ans = 0

for i in lst[::-1]:
    ans += score // i
    score = score % i

print(ans)


