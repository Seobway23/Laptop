import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    #기준 정하기, 가장 중심으로 잡음
    si = sj = N//2

    j = 0 ; ans = 0; #j는 행, ans 는 cnt 합
    #위, 아래 더 하기
    while sj != j:
        for i in range(si-j, si +j +1):

            ans += arr[j][i]
            dd = arr[N-j-1][i]
            ans += arr[N-j-1][i]
        j += 1

    #중앙 더하기
    for k in range(N):
        ans += arr[sj][k]

    print(f"#{test_case} {ans}")

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = mid = end = N // 2
    count = 0
    for i in range(N):
        for j in range(start, end + 1):
            count += arr[i][j]
        if i < mid:
            start -= 1
            end += 1
        elif i >= mid:
            start += 1
            end -= 1

    print(f'#{t + 1} {count}')