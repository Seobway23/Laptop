'''
#1 -1
#2 -1
#3 3

주변 8개 cnt 가 되어야 ans+=1
1. arr 0 패딩
2. for 문으로 cnt 하기
3. 8개가 되지 않았을 때 -1 출력

'''

def algorithm1(arr):
    ans=[]
    mx=0
    mn=10
    for i in range(1, N+1): # i, j 행렬 1부터 N까지
        for j in range(1, N+1):
            cnt = 0     #봉우리 cnt 세기
            for si in range(i-1, i+2): #i-1부터 i+1까지
                for sj in range(j-1, j+2):#j-1부터 j+1까지
                    if arr[i][j] > arr[si][sj]: #주변보다 높으면 cnt+=1


                        cnt += 1
            #봉우리 확인
            if cnt == 8:
                ans.append(arr[i][j])

                if mx < arr[i][j]:
                    mx = arr[i][j]

                elif mn > arr[i][j]:
                    mn = arr[i][j]



    #예외 처리, 1 이상일 경우 ans 반환
    if len(ans) > 1:
        return mx - mn

    else: # 아니라면 -1 반환
        return -1


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr= [[10]*(N+2)]+[[10]+list(map(int, input().split())) + [10] for _ in range(N)] +  [[10]*(N+2)]#0 패딩
    print(f"#{test_case} {algorithm1(arr)}")