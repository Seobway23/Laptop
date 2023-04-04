import sys
sys.stdin = open('input.txt','r')

'''
1 <= N <= 100,000
1 <= M <= 100,000
'''

N_1 = int(input())
lst_1 = set(map(int, input().split()))
N_2 = int(input())
lst_2 = list(map(int, input().split()))
ans = 0
for i in lst_2:
    if i in lst_1:
        print(1)
    else:
        print(0)
