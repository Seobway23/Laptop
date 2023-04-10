import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
lst = [0] * T
for t in range(T):
    w, B = input().split()
    A = int(w)
    lst[t]= [A, B, w]

lst.sort(key=lambda x: (x[0], x[2]))
for i in lst:
    print(*i[:-1])