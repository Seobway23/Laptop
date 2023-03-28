import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split()) #N 컨테이너수 , M 트럭 수
    dummy = list(map(int, input().split())) # N개의 화물의 무게
    truck = list(map(int, input().split())) # M개의 트럭의 적재수
    v_dummy = [0] * 100
    v_truck = [0] * 100
    dummy.sort(reverse=True)
    for i in range(len(dummy)):
        v_dummy[i] = dummy[i]

    truck.sort(reverse=True)

    for i in range(len(truck)):
        v_truck[i] = truck[i]

    sm = 0
    j = 0
    while True:
        if v_dummy[j] == 0:
            break

        if v_truck[j] >= v_dummy[j]:
            sm += v_dummy[j]
            v_truck.pop(0)
            v_dummy.pop(0)

        else:
            v_dummy.pop(0)

    print(f"#{test_case} {sm}")

