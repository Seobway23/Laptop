from collections import deque

arr1 = deque(['-1'] * 8)


arr =  [deque(['-1']*8)] + [deque(list(input())) for _ in range(4)] + [deque(['-1']*8)]
k = int(input())


def rotate(gear, cir, prev=None):
    # 종료 조건
    if gear == 0 or gear == 5:
        return

    # 9시 방향 : 6, 3시 방향 : 2
    # 왼쪽 판단
    if prev != gear - 1 and arr[gear][6] != arr[gear-1][2]: # if N - S:
        # next gear -> move
        rotate(gear -1, -cir, gear)


    # 오른쪽  판단
    if prev != gear + 1 and arr[gear][2] != arr[gear + 1][6]:
        rotate(gear + 1, -cir, gear)

    # current gear -> cir directional rev -> only first
    arr[gear].rotate(cir)

for _ in range(k):
    gear, cir = map(int, input().split())
    # rotate
    rotate(gear, cir)

print(sum(2**(k -1) if arr[k][0] == '1' else 0 for k in range(1, 5)))