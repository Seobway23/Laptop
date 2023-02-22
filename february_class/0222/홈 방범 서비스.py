import sys
sys.stdin = open('input.txt', 'r')

T = 1
for test_case in range(1, T+1):
    # N 도시의 크기 5<=N<=20, M 하나가 지불할 수 있는 비용 1 <= M <= 10
    N, M = map(int, input().split())
    arr = [ list(map(int,input().split())) for _ in range(N)]
    print(arr)

