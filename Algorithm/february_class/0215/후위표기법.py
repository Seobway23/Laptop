'''
3
9+5*2+1+3*3*7*6
4+4*3*4*9+2+7*4*7+7*7*9*5*2+8*8
2+3+9*9+8+2*1+3*2*3*1+3*3+1+2+3*6*2*7*4+9
'''

import sys
sys.stdin=open("input.txt", "r")

def ans_stk(str1):

    for i in str1:
            if i in list(tlst.keys()): #만약 +, *가 있다면

                if stk: #stk가 들어있으면 token 값 대로 넣고 빼기
                    if tlst[stk[-1]] < tlst[i]:
                        stk.append(i)

                    else:
                        while stk and tlst[stk[-1]] >= tlst[i]:
                            alst.append(stk.pop())
                        #while이 끝나면 추가
                        stk.append(i)

                else: #stk가 없으면 stk에 추가
                    stk.append(i)

            else: #숫자라면 alst에 숫자 추가
                alst.append(i)


    while True: #다 끝나고 stk에 있는 연산자들을 top부터 꺼내서 alst에 붙이기
        if stk:
            alst.append(stk.pop())

        else:
            break




T=int(input())
for test_case in range(1,T+1):
    str1=input()
    tlst={'+':1, '*':2}

    #To make stack, lst
    stk=[]
    alst=[]
    ans_stk(str1)
    ans=''
    for i in alst:
        ans += i

    #print(alst, end='')
    print(f"#{test_case} {ans}")

