'''
N=x^3이 되는 양의 정수 X를 구해라

입력 받으면 어떻게 나누지?

이미 있는 수에다가 비교할 수 있겠네

나누는게 아니라, 나눠지면, 그 수의 세제곱이랑 비교
'''

import sys
sys.stdin = open('input.txt', 'r')


def triple(N):
    num = 0

    if N==1:
        return 1

    for i in range(2,10**6): #2부터 9까지
        if N%i == 0:
            num = i

        if num ** 3 == N:
            return num


    else:
        return -1



T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    print(f"#{test_case} {triple(N)}")

