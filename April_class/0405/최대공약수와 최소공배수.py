import sys
sys.stdin=open('input.txt', 'r')

'''
10000이하의 수

최대공약수 -> for 나누기
최소공배수 -> 

24 -> 1, 2, 3, 4, 6, 8, 12, 24
18 -> 1, 2, 3, 6, 9, 18

'''

A, B = map(int,input().split())

A_1 = []
B_1 = []
for i in range(1, A+1):
    if A%i == 0:
        A_1.append(i)

for j in range(1, B+1):
    if B % j == 0:
        B_1.append(j)

# 최대 공약수
min_mul = 0
for k in A_1:
    if k in B_1:
        if min_mul < k:
            min_mul = k
print(min_mul)

# 최소 공배수
for l in range(1, 10001):
    num = min_mul*l
    if num >= A and num >=B:
        if num % A == 0 and num% B == 0:
            break

print(num)

