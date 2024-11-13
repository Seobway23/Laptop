import math

n = int(input())
peoples = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for man in peoples:
    # 감독관
    man -= B
    ans += 1

    # 부 감독관이 필요한 경우
    if man > 0:
        ans += math.ceil(man / C)

print(ans)