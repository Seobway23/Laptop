import sys
sys.stdin = open('input.txt', 'r')

'''
push X: 정수 X 를 스택에 넣는 연산
pop: 스택에서 가장 위에있는 정수를 빼고 그 수를 출력한다.

'''

T = int(sys.stdin.readline())
stk = []
for _ in range(T):
    A, *B = sys.stdin.readline().split()

    if B:
        b = int(*B)
        stk.append(b)

    elif A == 'pop':
        if stk:
            t = stk.pop()
            print(t)
        else:
            print(-1)

    elif A == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)

    elif A == 'empty':
        if stk:
            print(0)
        else:
            print(1)

    elif A == 'size':
        print(len(stk))



