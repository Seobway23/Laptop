import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# from collections import deque

# 1 실패
# def dp(sm, d):
#     global ans
#     if d > N-1:
#         return
#     if d == N-1:
#         if sm < ans:
#             ans = sm
#         return
#
#     for i in range(N-1):
#         for j in range(i+1,N):
#             if lst[i] !=0 and lst[j] != 0:
#                 ij = lst[j]
#                 ii = lst[i]
#                 cnt = ii + ij
#                 lst.pop(j)
#                 lst[j] = 0
#                 lst[i] = cnt
#                 dp(sm+cnt, d + 1)
#                 lst[j] = ij
#                 lst[i] = ii
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     ans = 10000*500
#     dp(0, 0)
#     print(ans)

# 2 실패
# sort, 최솟값
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     ans = []
#     while len(lst) > 1:
#         lst.sort()
#         t = lst[0] + lst[1]
#         ans.append(t)
#         lst.append(t)
#         lst.pop(0)
#         lst.pop(0)
# print(sum(ans))

# 3 연속적으로/ 실패
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     ans = 0
#     k= 0
#     while k != N-1:
#         k += 1
#         sm = [500 * 10000, 0]
#         for i in range(len(lst)-1):
#             n = lst[i] + lst[i+1]
#             if n < sm[0]:
#                 sm = ([n, i])
#
#         lst[sm[1]] = sm[0]
#         lst.pop(sm[1]+1)
#         ans += sm[0]
#     print(ans)

#
# # 4 DP
# T = int(input())
# for test_case in range(1, T+1): #
#     N= int(input())
#     lst = list(map(int,input().split()))
#     DP = [[0]*(N) for _ in range(N)]
#     # DP[i][j] => i에서 j까지 합하는데  필요한 최소 비용
#     for i in range(1, N+1):
#         for j in range(N+1-i):
#             DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + sum(list(lst[i] for i in range(j,j+i-1+1)))
#
#     print(DP[1][N])
#
#
#


def solve():
    N, A = int(input()), [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i]

    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    DP = [[0 for i in range(N + 1)] for _ in range(N + 1)]
    for i in range(2, N + 1):  # 부분 파일의 길이
        for j in range(1, N + 2 - i):  # 시작점
            DP[j][j + i - 1] = min([DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]) + (
                        S[j + i - 1] - S[j - 1])

    print(DP[1][N])


for _ in range(int(input())):
    solve()





