from collections import deque

n, w, l = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(arr)
bridge = deque([0] * w)
cnt = 0

# bridge 를 기준 으로 하자,
while q:
    if sum(bridge) > l:
        bridge.pop()
        bridge.appendleft(0)

    else:
        bridge.pop()
        if q[0] + sum(bridge) <= l:
            bridge.appendleft(q.popleft())
        else:
            bridge.appendleft(0)
    cnt += 1
    
print(cnt + w)