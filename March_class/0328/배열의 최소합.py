import sys
sys.stdin = open('input.txt', 'r')

def recur(cnt, sm): #cnt 가 행
    global min_sum
    for i in range(N): #i 는 열
        if visited[i] == 0:
            visited[i] = 1
            sm += arr[cnt][i]

            # 재귀
            if min_sum > sm:
                if cnt == N-1:
                    min_sum = sm

                else:
                    recur(cnt+1, sm)

            # 다음 열을 위한 초기화
            visited[i] = 0
            sm -= arr[cnt][i]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_sum = 10*N**2
    recur(0,0)
    print(f'#{test_case} {min_sum}')