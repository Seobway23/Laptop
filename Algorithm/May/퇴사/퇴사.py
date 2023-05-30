import sys
sys.stdin = open('input.txt')


def dfs(index, sm):
    global N, ans
    # 종료 조건
    if index == N:
        # 갱신
        if ans < sm:
            ans = sm
            return

    # return 조건
    if index > N-1:
        return

    # 순회 추가 조건
    # if lst[index][0] not in visited:
    dfs(index+1, sm)
    dfs(index + lst[index][0], sm + lst[index][1])


N = int(input())
lst = []
ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

dfs(0, 0)
print(ans)
# print(lst)

