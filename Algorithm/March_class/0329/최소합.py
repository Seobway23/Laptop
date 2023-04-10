import sys
sys.stdin = open('input.txt', 'r')

def recur(i,j, sm): #i 행
    global min_sum
    #종료 조건
    if sm > min_sum:
        return
    if i > N-1 or j > N-1:
        return

    sm += arr[i][j]
    if i == N-1 and j == N-1 and sm < min_sum:
        min_sum = sm

    recur(i, j+1, sm)
    recur(i+1, j, sm)



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 13*N
    recur(0, 0, 0)
    print(f"#{test_case} {min_sum}")