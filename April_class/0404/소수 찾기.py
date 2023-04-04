import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))

#갯수 세기
cnt = 0
for j in lst:
    ans = 0
    if j > 1: #1 이상일 때
        for i in range(2, j):
            if j % i == 0:
                ans += 1
        if ans == 0:
            cnt += 1

print(cnt)