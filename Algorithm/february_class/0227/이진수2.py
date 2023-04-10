import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    i = 0; bt_N = ''
    while N > 0: #판별 시작
        #끝 조건
        if len(bt_N) > 12:
            bt_N = 'ooverflow' #1인덱스부터 해야하니까 o 앞에 추가...
            break

        if 2**i <= N: # N보다 작으면 빼고 비트에 추가
            N -= 2**i
            bt_N += '1'

        else: #아니면 0추가
            bt_N += '0'
        # 다 끝나면 i -= 1
        i -= 1

    print(f"#{test_case} {bt_N[1:]}")



