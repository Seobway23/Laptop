import sys
sys.stdin = open('input.txt', 'r')


'''
8까지가 아니라 5까지가 반복이었음...
'''

def pw(lst):
    idx = 0;
    while True:
        i = 0; cnt = 1; a = idx;
        while i < 8: #8번 반복하겠음
            if lst[a] < 0:  # 종료 조건
                lst[a] = 0
                return lst
            #계산
            lst[a] -= cnt
            cnt += 1
            a = (1 + a) % (len(lst))
            i += 1

        #원형 큐 기준 인덱스
        idx = (1 + idx) % (len(lst))



T = 2
for test_case in range(1,T+1):
    N=int(input())
    lst = list(map(int,input().split()))
    ans = list(pw(lst))
    print(f"#{test_case}", *ans)