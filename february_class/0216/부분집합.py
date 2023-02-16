import sys
sys.stdin=open('input.txt', 'r')


def f(i, k, s, t): # i 원소, k 집합의 크기, s i-1까지의 합, t 목표
    global cnt
    if s > t: #이미 목표보다 커진 경우
        return
    # elif s == t: # 합과 목표가 같은 경우 남은 원소 고려 X
    #     cnt += 1
    #     return

    if i == k:
        if s == t:  # 마지막에 같은 경우
            for j in range(k):
                if bit[k]:
                    print( lst[j], end=' ')
            print()
            cnt += 1
        return cnt
    else:           # 다른 경우\
        bit[i]=1
        f(i+1, k, s + lst[i], t)  #lst[i]가 포함
        bit[i]=0
        f(i+1, k, s, t)           #lst[i]가 미포함


T=int(input())
for test_case in range(1,T+1):
    N, k = map(int,input().split()) #N 원소의 수, K 부분집합의 합
    lst = list(map(int,input().split()))
    cnt=0
    bit=[0]*(len(lst)+1)
    f(0, N, 0, k)
    print(f'#{test_case} {cnt}')
