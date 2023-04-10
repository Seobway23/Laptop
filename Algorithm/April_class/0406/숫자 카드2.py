import sys
sys.stdin = open('input.txt', 'r')

'''
# 범위 -천만부터 + 천만
# N 숫자의 갯수 50만개까지
'''

# 딕셔너리 추가해도 안됨;
# N = int(input())
# N_lst = list(map(int, input().split()))
# M = int(input())
# M_lst = list(map(int, input().split()))
# v = [0] * M
#
# dic = {}
# for i in range(len(M_lst)):
#     dic[M_lst[i]] = i
#
# for i in N_lst:
#     if i in M_lst:
#         dd = dic[i]
#         v[dic[i]] += 1
#
# print(*v)
# # 시간 초과 해결 못했음


# 이진 탐색
def bs(l, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if l[mid] == target:
        return cnt.get(target)
    elif l[mid] > target:
        return bs(l, target, start, mid-1)
    else:
        return bs(l, target, mid+1, end)

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

cnt = {}
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    print(bs(a, i, 0, len(a)-1), end=' ')