import sys
sys.stdin=open('input.txt', 'r')

def f(n, sm, cnt):  # n 시작 원소, n-i의 sm 부분집합의 합
    global ans
    #[0] 가지치기는 제일 위쪽에서 한다.
    if sm>K or cnt>M:
        return

    if n == N:#개수가 같으면,
        if sm == K and cnt==M: #합이 같으면, cnt+1
            ans += 1
            return

    elif sm>K: # 부분집합의 합이 목표보다 더 크면
        return
    else:
        f(n + 1, sm + lst[n], cnt + 1)   #포함인 경우
        f(n + 1, sm + 0, cnt + 0)            #미포함인 경우

T=int(input())
for test_case in range(1,T+1):
    M, K = map(int,input().split()) #N 원소의 수, K 부분집합의 합
    lst = [1,2,3,4,5,6,7,8,9,10,11,12]
    N=len(lst)
    ans=0
    f(0, 0, 0) # i 시작 원소 index, sm i-1까지의 합, cnt 원소의 갯수
    print(f'#{test_case} {ans}')

