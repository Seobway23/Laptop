import sys
sys.stdin = open('input.txt', 'r')
'''
6 12 12 // 603  -> 602가 나와야 함
6 1 6   // 602 -> 601이 나와야 함 
6 2 7   // 102 -> 102 맞음 
6 2 12  // 603 -> 602 나와야 함
'''
# 각방 층수, 각 층 방의 수, 몇번째 손님
T = int(input())
for _ in range(T):
    N, M, k = map(int,input().split())
    floor = k % N
    number = k//N + 1

    # floor 0이면 꼭대기 층
    if floor == 0:
        floor = N
        number -= 1

    print(floor * 100 + number)


