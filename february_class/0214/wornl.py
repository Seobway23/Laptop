import sys
sys.stdin=open("input.txt", "r")
t=1
for test_case in range(t):
    T, L = map(int,input().split())
    Link = list(map(int,input().split()))
    N=10
    arr=[[0]*(N+1) for _ in range(N+1)]

    #arr 생성
    for s in Link[::2]:
        arr[s][s+1] = 1


