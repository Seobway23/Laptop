import sys
sys.stdin = open('input.txt', 'r')

K, N = map(int,input().split())
A = [int(input()) for _ in range(K)]

# 시간초과로 안 되었음, 이진 탐색 써야 함
# num = 1; ans = 0; cnt = 0
# while True:
#     cnt = 0
#     for k in A:
#         cnt += k//num
#
#     if cnt >= N:
#         ans = num
#         num += 1
#
#     else:
#         break
#
# print(ans)
#
# # 오름차순 이분탐색

# 이진 탐색
# A.sort() # 굳이 다시 정렬보다 끝 위치만 쓰면 됨
start = 1; end = max(A) # 이분 탐색 처음과 끝

while start<= end: # 엔드가 더 클때까지 while문 돌리기
    mid = (start +end )//2 # 중간 위치
    cnt = 0 # 랜선 수
    for i in A:
        cnt += i // mid # 분할된 랜선 수

    if cnt >= N: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)