n, k = map(int, input().split())
lst = dict()

for i in range(1, n + 1):
    name = input()
    lst[i] = name
    # name, i 를 딕셔너리에 추가
    lst[name] = i

for _ in range(k):
    cmd = input()
    if cmd.isdigit():
        print(lst[int(cmd)])

    else:
        print(lst[cmd])
