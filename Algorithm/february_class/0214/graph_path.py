import sys
sys.stdin=open("input.txt", "r")

def stk(start):
    s=start
    v[s]=1
    alst.append(s)
    for j in range(V+1):
        if arr[s][j] and not v[j]:
            s=j
            v[s]=1
            alst.append(s)
            break

        else:
            if stk:
                s=stk.pop()

            else:
                break



T=int(input())
for test_case in range(1,T+1):
    V, E= map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]

    #arr 배열 <-
    for _ in range(E):
        s, e = map(int,input().split())
        arr[s][e]=arr[e][s]=1


    si, ej=map(int,input().split())

    stk=[]
    alst=[]
    v=[0]*(V+1)
    ans=0

    stk(si)
    print(f"#{test_case} {ans}")


