import sys
sys.stdin = open('input.txt', 'r')

def min_cal():
    return

def max_cal():
    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    calculation = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    mn = min_cal()
    mx = max_cal()

    print(f"{test_case} {mx-mn}")