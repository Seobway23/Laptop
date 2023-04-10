import sys
sys.stdin = open('input.txt', 'r')

def judge(lst):
    stack = []
    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append('(')

        elif lst[i] == ')':
            if stack:
                stack.pop()

            else:
                return 'NO'

    # 판별이 끝나고 stack이 남아있다면, no
    if stack:
        return 'NO'

    return 'YES'


N = int(input())
for test_case in range(N):
    lst = list(input())
    print(judge(lst))
