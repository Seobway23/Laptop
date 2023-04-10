import sys
sys.stdin = open('input.txt', 'r')

def cal(A, B, C, D):
    global min_sum, lst
    print(A, B, C ,D)
    dish1 = lst[A][B] + lst[B][A]
    dish2 = lst[C][D] + lst[D][C]
    print('dish2:',dish2, 'dish1:', dish1)
    if abs(dish1 -dish2) <min_sum:
        print('min_sum:', min_sum)
        min_sum = abs(dish1 -dish2)


def DFS(index, v, cnt):
    global arr
    # 1 종료 조건
    if cnt > len(arr):
        return

    # 2 그 다음에 계산 해
    if cnt == len(arr):
        if len(v) == 4:
            cal(v[0], v[1], v[2], v[3])
        return
    # 선택하지 않으면
    DFS(index+1, v, cnt + 1)
    # 선택하면
    if arr[index] not in v:
        v.append(arr[index])
        DFS(index+1, v, cnt + 1)

    # 2 그 다음에 계산 해
    return


T = int(input())
for test_case in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N)]
    min_sum= 1000
    v = []
    DFS(0,v,0)
    print(min_sum)
