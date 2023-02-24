import sys
sys.stdin = open('input.txt', 'r')


def tree(L):
    global ans
    cnt = P[L];
    #왼쪽 자식 노드가 있다면, 자식노드 호출
    if L*2 <= N:
        tree(2*L)

    #오른쪽 자식 노드가 있다면, 자식노드 호출
    if L * 2 +1 <= N:
        tree(2*L + 1)
    ans += cnt
    P[L] = ans

T= int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    P = [0] * (N + 1)
    #노드 입력
    for _ in range(M):
        A, B = map(int, input().split())
        P[A] = B
    ans = 0
    tree(L)
    print(f"#{test_case} {ans}")


