import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
q = []
for _ in range(T):
    A, *B = sys.stdin.readline().split()
    if B:

        q.append(int(*B))

    elif A == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)

    elif A == 'size':
        print(len(q))

    elif A == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif A == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif A == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)