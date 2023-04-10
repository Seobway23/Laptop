import sys
sys.stdin=open('input.txt', 'r')

def cal(str1):
    dic1 = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    dic2 = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    stk = []
    st = ''

    #1 후위 표기식 변환
    for i in str1:
        if i.isdigit(): #숫자면 st에 추가
            st += i

        else: #연산자이면, stk에 추가
            if stk:
                if i == ')':
                    while True:
                        if stk[-1] == '(':
                            stk.pop()
                            break

                        else:
                            st += stk.pop()

                else:
                    while dic2[stk[-1]] >= dic1[i]:
                        st += stk.pop()
                    stk.append(i)

            else:
                stk.append(i)

    #2 후위 표기식 계산
    ans = 0
    B = stk
    for j in st:
        if j.isdigit():
            stk.append(int(j))
        else:
            if len(st) >= 2:
                if j == '+':
                    stk.append(stk.pop() + stk.pop())

                elif j == '*':
                    stk.append(stk.pop() * stk.pop())

                else:
                    ans='error'
                    break

            else:
                ans='error'
                break
    #답 리턴
    if ans != 'error':
        ans = stk.pop()
    return ans


T=10
for test_case in range(1,T+1):
    N = int(input())
    str1 = input()
    print(f"#{test_case} {cal(str1)}")