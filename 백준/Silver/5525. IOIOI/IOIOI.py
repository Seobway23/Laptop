n = int(input())
l = int(input())
lst = input()
ans, cnt = 0, 0

i = 0
while i < l - 1:
    if lst[i: (i+2) + 1] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1

    else:
        i += 1
        cnt = 0


print(ans)