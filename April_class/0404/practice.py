# 그룹 나누기

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    fx = find_set(x)
    fy = find_set(y)
    if fx < fy:
        p[fy] = p[fx]
    else:
        p[fx] = p[fy]


T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]  # 0번도 들어가니 답에서 1 빼기
    lst = list(map(int, input().split()))

    for i in range(M):
        union(lst[2 * i], lst[2 * i + 1])  # p의 대표 번호를 바꿔주기

    v = set()

    for i in range(N + 1):
        v.add(find_set(i))  # 대표 번호의 개수 세기 = 집합의 개수

    print(f'#{case} {len(v) - 1}')