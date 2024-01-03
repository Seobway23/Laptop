from collections import deque

n = int(input())

lst = list(int(input()) for _ in range(n))
stack =deque()
ans_lst = []

for i in range(1, n + 1):
    stack.append(i)
    ans_lst.append("+")

    # 같으면 pop
    while True:
        if stack and lst and stack[-1] == lst[0]:
            stack.pop()
            lst.pop(0)
            ans_lst.append("-")

        else:
            break

if not lst:
    for i in ans_lst:
        print(i)

else:
    print("NO")