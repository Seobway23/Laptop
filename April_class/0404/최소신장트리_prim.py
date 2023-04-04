import sys
sys.stdin = open('input.txt', 'r')


def prim(ss):
    v[ss] = 1
    ret = 0

    for _ in range(V):  # 전체 노드 -1 개만큼 반복 처리
        mn, i_min = INF, 0
        for s in  range(V + 1):
            if v[s] == 1: # [1] mst 에 포함된 노드를 하나씩 처리 -> 포함안된 노드의 최솟값
                # 포함 안된 노드 중 최소 비용 연결 노드 찾기
                for e in range(V+1):
                    if v[e]==0 and mn > arr[s][e]:
                        mn, i_min = arr[s][e], e

        v[i_min] = 1
        ret += mn

    return ret

INF = 10 * 1001
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    v = [0] * (V+1)
    arr = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        hi, hj, w = map(int,input().split())
        # 특정 방향이 없기 때문에 둘다 w
        arr[hi][hj] = w
        arr[hj][hi] = w
    ans = prim(0)
    print(arr)
    print(f"#{test_case} {ans}")