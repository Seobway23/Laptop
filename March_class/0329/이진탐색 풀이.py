# check -> 풀이 -> 방향에 따라 달라지는 거를 cnt 해줘야 함

def binary_search(x):
    s, e = 0, n - 1
    check = 0
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            if check == 1:
                break
            check = 1
            e = mid - 1
        else:
            if check == 2:
                break
            check = 2
            s = mid + 1
    return False


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binary_search(num)
    print(f'#{tc} {total}')