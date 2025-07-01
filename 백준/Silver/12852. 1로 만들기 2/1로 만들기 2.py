n = int(input())

ans = [[] for _ in range(1_000_001)]

for i in range(2, 1_000_001):  # 1~3은 이미 처리했으므로 4부터 시작
    cand = []

    if i % 3 == 0:
        cand.append(ans[i // 3])
    if i % 2 == 0:
        cand.append(ans[i // 2])

    cand.append(ans[i - 1])

    # 가장 짧은 경로 선택
    best = min(cand, key=len)
    ans[i].extend(best)
    ans[i].append(i)

print(len(ans[n]))
print(*(ans[n][::-1] + [1]))