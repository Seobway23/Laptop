import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    #피자 데이터의 인덱스, 정보 리스트
    pizza=[]
    for i in range(len(lst)):
        pizza.append([i+1, lst[i]]) #숫자, 치즈 양

    #화덕
    fire= []
    std = 0

    ans = 0
    for _ in range(N):
        if len(fire) == N:
            break
        else:
            fire.append(pizza.pop(0))


    while len(fire) > 1:
        #화덕 채우기
        if pizza:

        #5개를 다 채운 후,
            if fire[std][1] != 0:
                fire[std][1] = fire[std][1]//2

            if fire[std][1] == 0:
                dd= fire[std][1]
                fire[std] = pizza.pop(0)




        else:
            if fire[std][1] != 0:
                dd = fire[std][1]

                ddd = fire[std][1]//2
                fire[std][1] = fire[std][1]//2

            if fire[std][1] == 0:
                fire.pop(std)
                std -= 1

        std = (std + 1) % len(fire)

    ans = fire[0][0]


    print(f'#{test_case} {ans}')


