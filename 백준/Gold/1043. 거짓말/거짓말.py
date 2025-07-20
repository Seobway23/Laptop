n, m = map(int, input().split())
knows = list(map(int, input().split()))[1::]
parties = [list(map(int, input().split()))[1::] for _ in range(m)]

# true가 되면 다시 순회
changed = True
while changed:
    changed = False
    for queries in parties:
        if any(p in knows for p in queries):
            for p in queries:
                if p not in knows:
                    knows.append(p)
                    changed = True

know_lst = set(knows)

# 정답 처리
ans = 0
for queries in parties:
    if not any(i in know_lst for i in queries):
        ans += 1

print(ans)
