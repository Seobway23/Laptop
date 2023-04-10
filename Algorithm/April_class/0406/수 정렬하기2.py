import sys
sys.stdin = open('input.txt', 'r')


## sort 정리
# N = int(input())
# lst = [0]*N
# for i in range(N):
#     A = int(input())
#     lst[i] = A
#
# lst.sort()
# for j in lst:
#     print(j)
#

## 선택 정렬 -> 2초 시간 초과
# N = int(input())
# arr = list(int(input()) for _ in range(N))
#
# for i in range(N-1, -1 + 1,-1): # i 는 N부터 0 + 1까지 -1 공차 -> 1번째일 때 i -1이 0이어야 하기 때문에
#     for j in range(i-1, -1, -1):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#
# for k in arr:
#     print(k)

from time import time

# bubble 정렬 -> 2초 시간 초과
#-> 반복할 때 리스트의 길이를 줄이지 않고 계속 돌아야 함 -> 이게 맞음

# N = int(input())
# arr = list(int(input()) for _ in range(N))
#
# for _ in range(N-1):
#     for i in range(N-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#
# for j in arr:
#     print(j)


#merge sort  split -> merge
# from time import time


def merge_sort(arr):
    if len(arr) < 2:
        return arr   # return arr 왜하는거? -> arr update

    mid = len(arr)//2   # 반 나눠서 분리할꺼니까
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merge_arr = []
    left = right = 0
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            merge_arr.append(left_arr[left])
            left += 1

        else:
            merge_arr.append(right_arr[right])
            right += 1

    # 나머지 넣어야지
    merge_arr += left_arr[left:]
    merge_arr += right_arr[right:]

    return merge_arr # merge_arr update


N = int(input())
arr = list(int(input()) for _ in range(N))
# a = time()
lst = merge_sort(arr)
# b = time()

# print(f"{b-a:.20}", 'sec')

for i in lst:
    print(i)