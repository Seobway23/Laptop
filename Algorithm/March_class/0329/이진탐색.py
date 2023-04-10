import sys
sys.stdin = open('input.txt', 'r')


def binary_search(arr, target):
    cnt = 0
    left = 0
    right = len(arr) - 1
    check = 0
    # 한쪽으로 두 번 들어가는 오류를 피하기 위해
    #check 변수 사용

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            cnt += 1
            return cnt

        elif arr[mid] > target:
            right = mid - 1
            if left <= right and arr[right] == target:
                cnt += 1
                return cnt

        else:
            left = mid + 1
            if left <= right and arr[left] == target:
                cnt += 1
                return cnt

        return cnt


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    for num in A:
        ans += binary_search(B, num)

    print(f"#{test_case} {ans}")
