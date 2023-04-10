import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    v = []
    for _ in range(N):
        s, e = map(int, input().split())
        v.append([s, e])

    # 인덱스 1을 기준으로 정렬하는 방법
    v.sort(key=lambda x: x[1])

    # 먼저 종료를 우선으로 하면 그리디로 풀 수 있음
    si = 0; cnt = 0
    for i, j in v:
        if si <= i:
            cnt += 1
            si = j

    print(f"#{test_case} {cnt}")