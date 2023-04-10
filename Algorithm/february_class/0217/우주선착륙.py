import sys
sys.stdin=open('input.txt', 'r')

def landing(arr):
    ans=0
    for i in range(1, N+1):
        for j in range(1, M+1):
            # cnt시작
            cnt=0
            for si in range(i-1,i+1+1):
                for sj in range(j-1, j+1+1):
                    if arr[i][j] > arr[si][sj]:
                        cnt += 1

            if cnt >= 4:
                ans += 1

    return ans


T=int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr= [[10]*(M+2)] + [[10] + list(map(int,input().split())) + [10] for _ in range(N)] + [[10]*(M+2)]
    print(f"#{test_case} {landing(arr)}")
