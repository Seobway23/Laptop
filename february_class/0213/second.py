import sys
sys.stdin=open("input.txt", "r")

def abs(x):
    if x>0:
        return x
    else:
        return -x

T=int(input())
for test_case in range(1,T+1):
    N=int(input()) # 두더지 반복 횟수
    si, sj = map(int, input().split())
    ans=0
    for _ in range(N):
        ei, ej, k = map(int,input().split())

        # 1) 이동 가능한 경우,
        # 2) 열은 이동 가능/ 행은 부분이동
        # 3) 열 부분적으로 이동

        if abs(si-ei)+abs(sj-ej)<=k: # 목적지가지 이동가능
            si,sj=ei,ej
            ans+=1

        elif abs(sj-ej)<=k:         #열 방향으로는 완전히 이동, 행 방향은 부분적으로만 이동
            rem = k - abs(sj-ej)    # 열방향 이동후 남은 거리(0이상인 거리)
            sj=ej                   # 열방향 이동

            if si>ei:       # si>ei 이동한다면 좌표가 줄어들면서 이동
                si-=rem

            else:
                si+=rem

        else:                       #열방향만 부분적으로 이동
            if sj>ej:       # sj>ej : 이동한다면 좌표가 줄어들면서 이동
                sj-=k
            else:
                sj+=k

    print(f"#{test_case} {ans}")





