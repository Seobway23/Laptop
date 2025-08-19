n, k = map(int, input().split())

p = 2
cnt = 0
arr = [1] * 1001

while p <= n:
    # 방문 표시
    if arr[p]:
        cnt += 1
        arr[p] = 0

        # 바로 종료 처리
        if cnt == k:
            print(p)
            exit()

    # 배수 처리
    mul = 2
    step = p * mul
    while step <= n:
        if arr[step]:
            cnt += 1
            arr[step] = 0

            # 바로 종료 처리
            if cnt == k:
                print(step)
                exit()



        mul += 1
        step = p * mul

    # 배수 처리 후 + 1
    p += 1
