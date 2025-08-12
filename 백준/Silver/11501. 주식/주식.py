t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = 0
    ans = 0

    # 뒤를 돌면서
    for i in reversed(arr):
        # max 갱신
        if i > mx:
            mx = i

        # 현재 max 빼기, ans 더하기
        else:
            ans += mx - i

    print(ans)
