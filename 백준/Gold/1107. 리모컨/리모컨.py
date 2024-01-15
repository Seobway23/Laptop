chn = int(input())
n = int(input())
if n >= 1:
    ban_num = list(map(int, input().split()))
else:
    ban_num = []

min_cnt = abs(100 - chn)

for nums in range(1000001):
    num = str(nums)

    for i in range(len(num)):
        if int(num[i]) in ban_num:
            break
    else:
        min_cnt = min(min_cnt, abs(int(num) - chn) + len(num))

print(min_cnt)
