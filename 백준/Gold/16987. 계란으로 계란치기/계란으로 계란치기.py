def check(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def dfs(dep, arr):
    global ans

    # 종료 조건
    if dep == n:
        ans = max(ans, check(arr))
        return

    # 깨졌다면 재귀 호출
    if arr[dep][0] <= 0:
        dfs(dep + 1, arr)
    # 안깨졌으면 다음 것 넘기기
    else:
        broken = True
        for i in range(n):
            if dep != i and arr[i][0] >0:

                broken = False
                arr[dep][0] -= arr[i][1]
                arr[i][0] -= arr[dep][1]
                dfs(dep + 1, arr)

                # 복원
                arr[dep][0] += arr[i][1]
                arr[i][0] += arr[dep][1]

        # for 문을 지나 전부 깼다면 마지막 n 호출
        if broken:
            dfs(n, arr)

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dfs(0, eggs)
print(ans)
