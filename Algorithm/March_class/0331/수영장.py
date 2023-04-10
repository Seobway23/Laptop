import sys
sys.stdin = open('input.txt', 'r')


def dfs(i, sm):
    global min_sum
    if i > 12:
        if sm < min_sum:
            min_sum = sm
        return

    dfs(i+1, sm + lst[i]*d1)
    dfs(i + 1, sm + 1*d2)
    dfs(i + 3, sm + d3)
    dfs(i + 12, sm + d4)




T = int(input())
for test_case in range(1, T+1):
    d1, d2, d3, d4 = map(int,input().split())
    lst = [0] + list(map(int, input().split()))
    min_sum = 3000*12
    dfs(0, 0)
    print(f"#{test_case} {min_sum}")

