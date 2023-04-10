import sys
sys.stdin = open('input.txt', 'r')

def team_sort(lst):
    for i in range(0,len(lst)-1,2):
        P1.append(lst[i])
        P2.append(lst[i+1])


def babygin():
    V1= [0]*10; V2 = [0]*10
    cnt_1 = 0; cnt_2 = 0

    for i in range(len(P1)):
        # V 추가
        V1[P1[i]] += 1
        V2[P2[i]] += 1

        #트리플렛
        if V1[P1[i]] == 3:
            return 1

        elif V2[P1[i]] == 3:
            return 2

        #run
        #P1
        if 10> P1[i]-2 >= 0 and V1[P1[i]] >= 1 and V1[P1[i]-1] >= 1 and  V1[P1[i]-2] >= 1:
            return 1

        elif 10 > P1[i]+2 and V1[P1[i]] >= 1 and V1[P1[i]+1] >= 1 and  V1[P1[i]+2] >= 1:
            return 1

        elif 10>P1[i]+1 and P1[i]-1 >= 0 and V1[P1[i]-1] >= 1 and V1[P1[i]] >= 1 and  V1[P1[i]+1] >= 1:
            return 1

        #P2
        if 10> P1[i]-2 >= 0 and V2[P1[i]] >= 1 and V2[P1[i]-1] >= 1 and  V2[P1[i]-2] >= 1:
            return 1

        elif 10 > P1[i]+2 and V2[P1[i]] >= 1 and V2[P1[i]+1] >= 1 and  V2[P1[i]+2] >= 1:
            return 1

        elif 10>P1[i]+1 and P1[i]-1 >= 0 and V2[P1[i]-1] >= 1 and V2[P1[i]] >= 1 and  V2[P1[i]+1] >= 1:
            return 1

    # 종료 조건2
    return 0




T = int(input())
for test_case in range(1,T+1):
    lst = list(map(int, input().split()))
    P1 = [];    P2 = []
    team_sort(lst)
    print(f"#{test_case} {babygin()}")
