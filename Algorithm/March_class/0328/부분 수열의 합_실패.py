import sys
sys.stdin = open('input.txt', 'r')
#재귀로 하니까 안됨 ㄷㄷ

def recur(n,i,sm):
    global cnt
    if n > N:
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            sm += lst[i]

            # K 만나면 그 함수는 끝!
            if sm == K:
                cnt += 1
            else:
                recur(n+1, i+1, sm)

            # 초기화
            v[i] = 0
            sm -= v[i]

T=int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    v = [0] * N
    cnt = 0
    recur(0, 0, 0)
    print(f"#{test_case} {cnt}")