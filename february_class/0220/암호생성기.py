'''
1사이클 시작 -> 1부터 8까지
2사이클 시작 -> 1부터 8까지


'''

def pw(lst):
    arr = lst
    while True:
        cnt = 1
        for _ in range(len(arr)):
            if arr[0] == 0 :
                return arr

            arr[0] -= cnt
            #만약 0보다 작다면,
            if arr[0] < 0:
                arr[0] = 0

            cnt += 1
            arr.append(arr.pop(0))










import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst = list(map(int,input().split()))
    ans = list(pw(lst))
    print(f"#{test_case}", *ans)