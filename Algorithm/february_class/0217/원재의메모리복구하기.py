'''
1. 인덱스접근 str 이 1인지 파악
2. 처음 1인 지점은 for문을 통해 인덱스 파악
 그 지점이 시작 위치 i
3-1. 시작 위치부터 시작-> 1이라면, 계속 1인지 파악 >>1이 아니라면, cnt+=1 인덱스 위치 저장
3-2.                   0이라면, 계속 0인지 파악 >> 0이 아니라면 cnt+=1 인덱스 위치 저장
그리고 나서 cnt return 하면 됨

'''
import sys
sys.stdin=open('input.txt', 'r')


def bit_cal(i, N, cnt):
    global str1

    if i == N-1:
        return cnt
        # if str1[i] == str1[i + 1]:
        #     return cnt
        # else: #str1[i] == str1[i + 1]:
        #     return cnt +1

    else:
        if str1[i] == str1[i+1]:
            return bit_cal(i+1, N, cnt)

        elif str1[i] != str1[i+1]:
            return bit_cal(i+1, N, cnt+1)

# def cnt2(str1):
#     cnt=0
#     if str1[0] == '1':
#         cnt += 1
#
#     for i in range(N-1):
#         if str1[i] != str1[i + 1]:
#             cnt+=1
#
#     return cnt



T=int(input())
for test_case in range(1,T+1):
    str1 = input()
    N=len(str1)
    #bit_cal(0, N, str1, 0)
    cnt=0
    if str1[0] == '1':
        cnt+=1

    print(f"#{test_case} {bit_cal(0, N, cnt)}")