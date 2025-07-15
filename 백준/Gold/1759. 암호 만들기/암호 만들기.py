l, c = map(int, input().split())
words = list(input().split())
ans = []

# dfs
def dfs(idx, cnt, str):
    global ans

    # 종료 조건
    if idx == c:
        # str len == l & 자음 2개 이상, 모음 1개 이상
        if len(str) == l and cnt >= 1 and len(str) - cnt >= 2:
            new_str = "".join(sorted(str))
            ans.append(new_str)

        return

    # 선택
    dfs(idx + 1, cnt + 1 if words[idx] in ["a", "e", "i", "o", "u"] else cnt, str + words[idx])

    # 선택X
    dfs(idx + 1, cnt, str)

dfs(0, 0, "")

ans.sort()
for i in ans:
    print(i)
