import sys
sys.stdin=open('input.txt', 'r')

def landing(arr):
    cnt = 0
    for i in range(1, N+1):
        for j in range(1,M+1):
            #이제 판별 시작
            for fi in range(i-1,i+2): # i-1부터 i+1 가로 3
                for fj in range(j-1, j+2): # j-1부터 j+1 세로 3
                    dcnt = 0
                    d=arr[i][j]
                    dd=arr[fi][fj]
                    if arr[i][j] > arr[fi][fj]:
                        dcnt += 1

                    if dcnt>3:
                        cnt += 1
                        break

    return cnt




T=int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr= [[10]*(M+2)] + [[10] + list(map(int,input().split())) + [10] for _ in range(N)] + [[10]*(M+2)]

    print(f"#{test_case} {landing(arr)}")
