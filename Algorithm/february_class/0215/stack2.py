'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''

import sys
sys.stdin=open("input.txt", "r")

def stk_ans(S):
    while True:
        for e in range(V+1):
            #STEP4_1 if visited list is emtpy and path is, append e
            if not visited[e] and arr[S][e]:
                S=e
                stk.append(S)
                visited[S] = 1
                path_list.append(S)
                break
        #STEP4_2 if STEP4_1 is broken, to pop depending on the existence stk
        else:
            if stk:
                S=stk.pop()

            else:
                break


T=int(input())
for test_case in range(1,T+1):
    V, E= map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]
    #STEP1 input & writing arr
    for _ in range(E):
        v1, v2= map(int,input().split())
        arr[v1][v2]=1
    S, E= map(int,input().split())

    #STEP2 To make stack, visited and path_list
    stk=[]
    visited=[0]*(V+1)
    path_list=[]

    #STEP3 appending list at start
    stk.append(S)
    visited[S]=1
    path_list.append(S)
    ans=0
    #STEP4 To make the def: stk_ans(S)
    stk_ans(S)

    if E in path_list:
        ans=1

    #STEP5 print
    print(f"#{test_case} {ans}")



