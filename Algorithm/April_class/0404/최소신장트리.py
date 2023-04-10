import sys
sys.stdin = open('input.txt', 'r')


def find_set(n):
    if n == p[n]:
        return n
    p[n] = find_set(p[n])
    return p[n]


def union(s, e):
    p[find_set(e)] = find_set(s)


def kruskal():
    # [2] 링크 중심의 처리: w 값 오름차순으로 정렬 => 짧은 가중치값부터 처리
    arr.sort(key=lambda x: x[2])

    # [3] v개의 링크를 선택( 같은 그룹이 아닌 경우에만 선택)
    cnt = ret = 0
    for (s, e, w) in arr:
        # s, e가 연결되어 있지 않은 경우(사이클이 아닌 경우) 선택
        if find_set(s) != find_set(e):
            union(s, e)
            ret += w
            cnt += 1
            if cnt == V:
                return ret

    # 문제가 생기면 -1
    return -1


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    v = [0] * (V+1)
    arr = [list(map(int,input().split())) for _ in range(E)]

    # [1] make_set(): 각자 자기가 대표인 그룹 생성
    p = [n for n in range(V+1)]

    ans = kruskal()
    print(f"#{test_case} {ans}")