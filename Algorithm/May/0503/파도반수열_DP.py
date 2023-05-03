import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    N = [0 for _ in range(101+1)]
    N[0] = 1
    N[1] = 1
    N[2] = 1
    for i in range(3, 101+1):
        N[i] = N[i-2] + N[i-3]
    print(N[n-1])




