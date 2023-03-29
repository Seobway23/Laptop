'''
1. 피봇 정하기
2. 피봇 중간값이 선택되는게 효율이 좋음
맨 왼쪽 가운데, 중간 값 중에서 피봇을 정하는 방식이 있음

qsort는 정령이 되어 있는 경우, 안좋음
'''
import sys
sys.stdin = open('input.txt', 'r')

def quicksort(arr, start, end):
    if start >= end:
        return

    pivot = arr[(start+end)//2]
    left = start
    right = end


    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quicksort(arr, start, right)# 처음부터, r까지
    quicksort(arr, left, end)   # l부터 마지막까지

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print(f"#{test_case} {arr[N//2]}")

# 
# def binary_search(x):
#     s, e = 0, n - 1
#     check = 0
#     while s <= e:
#         mid = (s + e) // 2
#         if a[mid] == x:
#             return True
#         elif a[mid] > x:
#             if check == 1:
#                 break
#             check = 1
#             e = mid - 1
#         else:
#             if check == 2:
#                 break
#             check = 2
#             s = mid + 1
#     return False
#
#
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     a.sort()
#     total = 0
#     for num in b:
#         total += binary_search(num)
#     print(f'#{tc} {total}')