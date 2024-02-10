from collections import deque

n = int(input())
for _ in range(n):
    cmd = input()
    l = int(input())
    lst = input()
    if lst == "[]":
        lst = deque()

    else:
        lst = deque(list(map(int, lst[1:-1].strip().split(","))))

    R = 0
    for co in cmd:
        if co == "R":
            R += 1

        else:
            if lst:
                if R % 2 == 1:
                    # 홀수 이면 뒤에꺼 빼기
                    lst.pop()

                else:
                    # 짝수 이면 앞에거 빼기
                    lst.popleft()

            else:
                lst = "error"
                break

    if lst == "error":
        print(lst)

    else:
        if R % 2 == 1:
            lst.reverse()
            print("[", end="")
            print(*lst, sep=",", end="")
            print("]")

        else:
            print("[", end="")
            print(*lst, sep=",", end="")
            print("]")


