import sys
sys.stdin = open('input.txt', 'r')
'''
자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수?
'''
def dfs(index, sm):
    global ans
    #만약 인덱스가 범위와 같다면
    if index == N:
        if sm == K:
            ans += 1
            #print(sm)
        return

    # sm 포함 하는지 안하는 지는 합으로 판단
    dfs(index + 1, sm)
    dfs(index + 1, sm + lst[index])


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f"#{test_case} {ans}")