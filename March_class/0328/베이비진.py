import sys
sys.stdin=open('input.txt', 'r')

def babygin():
    for i in range(0, len(lst) - 1, 2):
        V1[lst[i]] += 1
        V2[lst[i + 1]] += 1
        P1 = lst[i]
        P2 = lst[i+1]

        # triplet
        if V1[P1] == 3:
            return 1
        elif V2[P2] == 3:
            return 2

        #run
        #P1
        if 10>P1+2 and V1[P1] >=1 and V1[P1+1] >=1 and V1[P1+2] >= 1:
            return 1
        elif P1-2>=0 and V1[P1] >=1 and V1[P1-1] >=1 and V1[P1-2] >= 1:
            return 1
        elif 10>P1+1 and P1-1 >=0 and V1[P1] >=1 and V1[P1-1] >=1 and V1[P1+1] >= 1:
            return 1
        #P2
        if 10>P2+2 and V2[P2] >=1 and V2[P2+1] >=1 and V2[P2+2] >= 1:
            return 2
        elif P2-2>=0 and V2[P2] >=1 and V2[P2-1] >=1 and V2[P2-2] >= 1:
            return 2
        elif 10>P2+1 and P2-1 >=0 and V2[P2] >=1 and V2[P2-1] >=1 and V2[P2+1] >= 1:
            return 2
    # 무승부이면
    return 0

T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    V1 = [0] * 10; V2 = [0] * 10
    print(f"#{test_case} {babygin()}")