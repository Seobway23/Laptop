import sys
sys.stdin=open("input.txt", "r")

def cal_result(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b==0:
            ans='error'
            return ans
        else:
            return int(a/b) # 문제를 잘 안봤음... int로 바꿔야 하는데 못바꿨음ㅠㅠ


def stk_num(str1):
    for i in str1:
        AAAA=number
        if i == '.':    # . 가 나오면 마지막 pop하고 ans 리턴
            if len(number)==1:
                ans = number.pop()
                return ans

            else:
                ans='error'
                return ans


        else:           # .가 아니라면
            if i in dic:    #str1에서 뽑은게 연산자라면
                if len(number) < 2: # 숫자 stack에 2개가 아니라면 error 출력
                    ans = 'error'
                    return ans

                else:       # 2개라면 연산하고, 이전 숫자들 pop해서 제거
                    A = cal_result(int(number[-2]), int(number[-1]), i)
                    if A=='error':
                        break
                    number.pop()
                    number.pop()
                    number.append(A)  # 연산을 한 후 number에 추가



            else:
                number.append(i)

    if number:
        ans='error'
        return ans


dic=['+','-','*','/']
T=int(input())
for test_case in range(1,T+1):
    str1= list(map(str,input().split()))

    ans=0
    number=[]
    print(f"#{test_case} {stk_num(str1)}")







