import sys
sys.stdin = open('input.txt', 'r')


while True:
    lst = list(map(int, input().split()))
    lst.sort()

    if lst ==[0,0,0]:
        break
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('right')

    else:
        print('wrong')