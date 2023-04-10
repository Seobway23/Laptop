import sys
sys.stdin=open('input.txt', 'r')
# #뒤를 기준으로 보기
# T= int(input())
# for test_case in range(1,T+1):
#     N= int(input())
#     lst= list(map(int,input().split()))[::-1] # 거꾸로 가져오겠다
#
#     ans = 0; mx = 0;
#     for n in lst:
#         if mx > n:
#             ans += mx-n
#         else:
#             mx = n
#
#     print(f'#{test_case} {ans}')


#앞을 기준으로 보기
#


T= int(input())
for test_case in range(1,T+1):
    N= int(input())
    lst= list(map(int,input().split()))
    i = 0; ans = 0;
    while i < N:
        i_mx = i
        # 맥스 값 찾기
        for j in range(i+1,N):
            if lst[i_mx]<lst[j]:
                i_mx = j

        # 더하기
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]

        i = i_mx + 1


    print(f"#{test_case} {ans}")