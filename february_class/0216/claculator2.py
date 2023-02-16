import sys
sys.stdin=open('input.txt','r')

def calculator(a, b, k):
    if k=='+':
        return a + b
    if k == '-':
        return a - b
    if k == '*':
        return a * b
    if b!=0 and k=='/':
        return int(a/b)
    else:
        return 'error'

def stk_opr(str1):
    # stack and list 만들기
    global dic_opr
    stk=[];
    number=[];


    for i in str1:
        if i in list(dic_opr.keys()): #0 i가 연산자라면
            if stk: #1stk이 있다면
                while stk and dic_opr[stk[-1]] >= dic_opr[i]: #2 token값이 작거나 같으면
                    B=stk.pop()                     # top의 stk 꺼내기
                    number.append(B)                # 꺼낸 것 number에 저장
                #while이 끝났으면 추가
                stk.append(i)

            else:   #1 stk가 없다면 연산자 stk에 저장
                stk.append(i)
        else:       #0 i가 숫자라면
            number.append(int(i))

    while True: #위 stk과 number를 분리하는 작업이 다 끝난 후에도 stk가 남아있다면 꺼내준다.
        if stk:
            number.append(stk.pop())
        else:   #
            if stk:
                S=stk.pop()
                number.append(S)

            else: #함수의 return값은 number로 한다.
                return number

def stk_sum(alst): # sum define
    num_list = alst
    num_list.append('.')
    num=[]
    global dic_opr

    for i in alst:
        if i == '.': #0 마지막 . 을 만나면
            if len(num)==1: #숫자가 하나이면 num반환
                return num

            else:           #하나가 아니라면 에러
                return 'error'



        else: #0 마지막이 아니면 연산 시작
            if i in list(dic_opr.keys()): #1 i가 연산자라면
                if len(num)>=2: #오류 검출/ 숫자는 2개 이상
                    A=calculator(num[-1],num[-2],i)
                    num.pop() #1번째 숫자 빼내기
                    num.pop() #0번째 숫자 배내기
                    num.append(A) #방금 계산한 A num에 넣기

                else: #오류 검출 2개가 아니면 연산 불가
                    return 'error'

            else: #숫자라면
                num.append(i)



T=10
for test_case in range(1,T+1):
    dic_opr = {'+': 1, '*': 2}
    N=int(input())
    str1=input()
    D = stk_sum(stk_opr(str1))
    print(f"#{test_case}", *D)