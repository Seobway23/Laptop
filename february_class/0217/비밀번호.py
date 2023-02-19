import sys
sys.stdin=open('input.txt', 'r')

def password(N, num):
    stk = []
    ans = ''
    for i in num:
        if stk: # 스택이 있으면
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)

        else: #스택이 없으면 스택에 추가
            stk.append(i)

    for i in stk:
        ans+=i

    return ans

T=3
for test_case in range(1,T+1):
    N, num = input().split() # N: num의 길이, num 문자열 숫자
    ans=password(N, num)

    print(f'#{test_case} {ans}')
    # print(f'#{test_case}', end= ' ')
    # print(*ans, sep='')

