import sys
sys.stdin = open('input.txt', 'r')

def babygin(v):
    global cnt
    # triplet 판별
    for i in range(10):
        if v[i] >= 3:
            cnt += 1
            v[i] -= 3

    j = 0
    while j < 10:
        #종료 조건
        if cnt == 2:
            return 1

        if v[j] == 1 and v[j+1] == 1 and v[j+2] == 1:
            cnt += 1
            j = j+3

        else:
            j += 1

    return 0

T = int(input())
for test_case in range(1, T+1):
    num = input()
    v = [0]*10
    for i in num:
        v[int(i)] += 1


    cnt = 0
    print(f'#{test_case} {babygin(v)}')



