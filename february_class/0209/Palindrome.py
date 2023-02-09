import sys
sys.stdin=open("input.txt", "r")
from pprint import pprint

T=10
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(8)]
    std_r = int(N/2) + 1
    cnt = 0
    for i in range(8):
        for j in range(8 - N+1):
            A=arr[i][j]
            B=arr[i][j + N - 1]

            if arr[i][j] == arr[i][j + N - 1]:
                cnt_h = 0
                for k in range(std_r):
                    C_1=j + k
                    D_1=j + N - 1 - k
                    C=arr[i][j + k]
                    D=arr[i][j + N - 1 - k]
                    if arr[i][j + k] == arr[i][j + N - 1 - k]:
                        cnt_h += 1

                    if cnt_h == std_r:
                        cnt += 1

            if arr[j][i] == arr[j + N - 1][i]:
                cnt_v = 0
                for k in range(std_r):
                    if arr[j + k][i] == arr[j + N - 1 - k][i]:
                        cnt_v += 1

                    if cnt_v == std_r:
                        cnt += 1

    print(f"#{test_case} {cnt}")