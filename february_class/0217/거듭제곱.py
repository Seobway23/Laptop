import sys
sys.stdin=open('input.txt', 'r')

def multi_cal(N, M): # N 밑, M 지수
    if M ==1:
        return N

    else:
        return N * multi_cal(N, M - 1)




T=10
for _ in range(1,T+1):
    test_case=int(input())
    N, M = map(int,input().split()) #N base  ,M exponential
    ans=multi_cal(N, M)
    print(f"#{test_case} {ans}")