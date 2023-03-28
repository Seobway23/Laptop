import sys
sys.stdin = open('input.txt', 'r')

def recur(cnt, sm):
    global min_sum, N
    for i in range(N):
        if v[i] ==0:
            v[i] = 1
            sm += arr[cnt][i]
            if min_sum > sm:
                if cnt == N-1:
                    min_sum = sm

                else:
                    recur(cnt + 1, sm)
            # 초기화
            v[i] = 0
            sm -= arr[cnt][i]

    return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    min_sum = 99 * N
    recur(0, 0)

    print(f"#{test_case} {min_sum}")