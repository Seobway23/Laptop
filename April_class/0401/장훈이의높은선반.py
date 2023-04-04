import sys
sys.stdin = open('input.txt', 'r')

#[2] 원하는 함수 짜기 DFS
def dfs(index, sm): #index는 lst의 인덱스, sm 은 합
    global ans
    # [2-1] 종료 조건
    if index == N: # N-1번째후 N번째 X일 때
        if sm >= B:
            if ans > sm:
                ans = sm # ans 갱신
        return

    # [2-2] 하부 호출
    dfs(index + 1, sm + lst[index])
    dfs(index + 1, sm)


# [1] 항상 top-down 방식으로 짤 것
# 필요한 것, 변수, 함수 생각하면서 시작
T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 10000*N
    dfs(0, 0)
    print(f"#{test_case} {ans-B}")