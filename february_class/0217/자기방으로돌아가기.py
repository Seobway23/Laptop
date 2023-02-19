import sys
sys.stdin=open('input.txt', 'r')

def r_time(N):




T=int(input())
for test_case in range(1,T+1):
    N= int(input()) # N: 돌아가야 할 학생 수
    for _ in range(N):
        cr, er = map(int,input().split())

    ans = r_time(N)
    print(f'#{test_case} {ans}')