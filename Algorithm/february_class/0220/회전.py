'''
N개의 숫자로 이루어진 수열
맨 앞의 숫자를 맨뒤로 보내는 작업을 M번했을 때 수열의 맨 앞에 있는 숫자는?

'''

def order(lst, M):
    for _ in range(M):
        lst.append(lst.pop(0))

    return lst[0]




import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f"#{test_case} {order(lst, M)}")



