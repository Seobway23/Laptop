import sys
sys.stdin=open('input.txt', 'r')

#가위바위보 def
def cal(A,B):
    if A > B:
        if A - B == 1:
            return A
        elif A - B == 2:
            return B

        else:
            return A

    else:
        if B - A == 1:
            return B
        elif A - B == 2:
            return A

        else:
            return A


def dvd(lst):
    global N

    if len(lst) == 1:
        return lst

    lst_next=[]
    if len(lst)%2==1:
        p = lst.pop()
        lst.append(p)
    for i in range(N//2+1):
        lst_next.append(cal(lst[2*i], lst[2*i+1]))


    return dvd(lst_next)




T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    dvd(lst)