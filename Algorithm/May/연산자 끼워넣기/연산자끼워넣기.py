import sys
sys.stdin = open('input.txt')


def dfs(index, total, plus, minus, multiply, divide):
    global mx, mn
    if index == N:
        mx = max(total, mx)
        mn = min(total, mn)
        return

    if plus:
        dfs(index+1, total + num_lst[index], plus-1, minus, multiply, divide)

    if minus:
        dfs(index + 1, total - num_lst[index], plus, minus - 1, multiply, divide)

    if plus:
        dfs(index + 1, total * num_lst[index], plus, minus, multiply - 1, divide)

    if plus:
        dfs(index + 1, int(total/num_lst[index]), plus, minus, multiply, divide-1)


N = int(input())
num_lst = list(map(int, input().split()))
operation = list(map(int, input().split())) # 연산자 +-*/
mx = -1e9
mn = 1e9
start_num = num_lst[0]

dfs(1, start_num, operation[0], operation[1], operation[2], operation[3])
print(mx)
print(mn)

