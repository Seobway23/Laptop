from collections import deque

n, k = map(int, input().split())
tmp = list(map(int, input().split()))
arr = deque(tmp)
v = deque([0] * (n * 2))
cnt, step = 0, 0


def rotate():
    # deque popleft, append
    # arr.appendleft(arr.pop())
    # v.appendleft(v.pop())
    arr.rotate(1)
    v.rotate(1)

    # remove machine, if machine is,
    if v[n - 1]: v[n-1] = 0

    # print(arr)
    # print(v)
    return

def move_machine():
    for i in range(n - 1, 0, -1):
        if v[i] == 0 and v[i - 1] == 1 and arr[i] > 0:
            # durability -= 1
            arr[i] -= 1
            v[i], v[i - 1] = 1, 0

    # remove machine
    if v[n - 1]:
        v[n - 1] = 0
    # print("--- move ---- ")
    # print(arr)
    # print(v)
    return

def add_machine():
    # add machine, if durability is,
    if not v[0] and arr[0] > 0:
        arr[0] -= 1
        v[0] += 1

    return


while  cnt < k:
    step += 1
    rotate()
    move_machine()
    add_machine()
    cnt = sum(1 if x == 0 else 0 for x in arr)
    # print(cnt, k)


print(step)