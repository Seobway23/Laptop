import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, cnt, sm):
    global ans
    if cnt > CNT or n == N+1:
        return

    if ans != 0:
        return

    if cnt == CNT and sm == K:
        ans += 1
        return

    # n은 1부터 12까지의 인덱스,
    # cnt 는 선택했는지 안했는지 여부
    # sm은 선택된 숫자들의 합
    dfs(n+1, cnt + 1, sm + n)
    dfs(n+1, cnt, sm)




# def dfs(n, cnt, sm):
#     global ans
#     # [1] 종료 조건 (n에 관련) => 정답처리
#     # 가지 치기
#     if sm > K or cnt > CNT:
#         return
#
#     if n == N:
#         if cnt == CNT and sm == K:
#             ans += 1
#         return
#
#     # [2] 하부 호출
#     # 사용하는 경우
#     dfs(n+1, cnt+1, sm+lst[n])
#     # 사용하지 않는 경우
#     dfs(n+1, cnt, sm)



T = int(input())
for test_case in range(1, T+1):
    CNT, K = map(int,input().split())
    N = 12
    # lst = [n for n in range(1, N+1)]
    #main loop에서는 dfs의 가장위 노드를 호출!
    ans = 0
    dfs(1, 0, 0)
    print(f'#{test_case} {ans}')

