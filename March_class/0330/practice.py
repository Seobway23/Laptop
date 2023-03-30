def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

            # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
            if i == len(left) and j == len(right):
                global cnt
                cnt += 1

    result += left[i:]
    result += right[j:]

    return result

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0  # 오른쪽 원소가 먼저 복사되는 경우의 수

    result = merge_sort(arr)

    print("#{} {} {}".format(test_case, result[n//2], cnt))
