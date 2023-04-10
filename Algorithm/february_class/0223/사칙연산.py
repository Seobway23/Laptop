import sys
sys.stdin = open('input.txt', 'r')


def cal(b, a, opr): # 사칙연산 func
    if opr == '+':
        return a + b

    elif opr == '-':
        return a - b

    elif opr == '*':
        return a * b

    elif opr == '/' and b != 0:
        return a / b

    return 'error'

def func(i): #재귀 func
    if c1[i]:
        func(c1[i])

    if c2[i]:
        func(c2[i])

    visited.append(dic[i])

def postfix(visited): #후위연산 계산
    num = []
    #종료 조건 -> .을 만났을 때 종료
    visited.append('.')

    for i in visited:
        #종료조건
        if i == '.':
            for i in num:
                ans = int(i)
            return ans

        if i.isdigit(): #숫자라면 num에 추가
            num.append(i)

        else: #연산자라면
            A =cal(int(num.pop()), int(num.pop()), i)
            num.append(A) #연산한 것을 num에 추가


T= 10 #int(input())
for test_case in range(1, T+1):
    N = int(input())
    # dic 설정
    dic = {}
    # 초기값 설정
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    #노드 길이 연결
    for _ in range(N):
        p, idx, *ab = input().split()
        dic[int(p)] = idx
        if len(ab) == 2:
            d = int(ab[0])
            b = int(ab[1])
            c1[int(p)] = int(ab[0])
            c2[int(p)] = int(ab[1])

        elif len(ab) == 1:
            c1[int(ab)] = ab

    visited=[]
    func(1)
    print(f"#{test_case} {postfix(visited)}")


