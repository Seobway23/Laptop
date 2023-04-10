from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
deque = deque()
for _ in range(T):
    A, *B = sys.stdin.readline().split()
    if A == 'push_front':
        deque.appendleft(*B)

    elif A == 'push_back':
        deque.append(*B)

    elif A == 'pop_front':
        if deque:
            t = deque.popleft()
            print(t)
        else:
            print(-1)

    elif A == 'pop_back':
        if deque:
            t = deque.pop()
            print(t)
        else:
            print(-1)

    elif A == 'size':
        print(len(deque))

    elif A == 'empty':
        if deque:
            print(0)
        else:
            print(1)

    elif A == 'front':
        if deque:
            print(deque[0])

        else:
            print(-1)

    elif A == 'back':
        if deque:
            print(deque[-1])

        else:
            print(-1)