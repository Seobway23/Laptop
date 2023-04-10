'''
최댓값을 찾아서 그 최댓값에서 계산하면 됨

'''

import sys
sys.stdin=open('input.txt', 'r')

def func(lst):
    stk=[]; sm=0; ans=0;
    #최대값 나올때까지 스택 쌓기
    for i in lst:
        if stk:
            if stk[-1] <= i:
                stk.append(i)

            else:
                D = stk.pop()
                n = len(stk)

                for i in stk:
                    sm += i
                ans += D * n - sm
                stk= []
                stk.append(i)

        else:
            stk.append(i)

    # 이제 계산
    D = stk.pop()
    n = len(stk)
    sj = 0
    for i in stk:
        sj += i
    ans += D * n - sj

    if ans<0:
        return 0

    return ans


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    print(f"#{test_case} {func(lst)}")