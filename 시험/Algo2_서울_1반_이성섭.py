'''
#1 0 1 0 3 2
#2 1 0 3 2 1 0 3
#3 0 1 2 3 0 1 0 3 2 1

NXN 벗어나지 못함
visited 만나면 끝
stack을 이용해 stk[-1]과 같지 않을 때 숫자 추가
'''


def algorithm2(arr):
    i = 0
    j = 0
    visited=[]
    stk=[]

    # 처음에 2와 3을 만났을 때 오류가 발생하기 때문에, 예외처리
    if arr[i][j] == 2 or arr[i][j] == 3:
        return stk

    while True:

        #if 0<=ni<N and 0<=nj<N and v[ni][nj] -> 활용 가능

        #범위를 벗어났다면
        if i > N-1 or i < 0: #0부터 N-1까지
            return stk
        elif j > N-1 or j < 0: #0부터 N-1까지
            return stk
        #visited를 만났다면
        elif [i, j] in visited:
            return stk

        else: #좌표 변경 + visited 추가

            if arr[i][j] == 0: #좌표값이 0이라면, 오른쪽 이동
                visited.append([i, j])
                if stk:
                    if stk[-1] != arr[i][j]:  # stk에 추가, 중복 제거
                        stk.append(arr[i][j])

                else:
                    stk.append(arr[i][j])
                j += 1

            elif arr[i][j] == 1: #좌표값이 1이라면, 아래쪽 이동
                visited.append([i, j])
                if stk:
                    if stk[-1] != arr[i][j]:  # stk에 추가, 중복 제거
                        stk.append(arr[i][j])

                else:
                    stk.append(arr[i][j])

                i += 1

            elif arr[i][j] == 2:  # 좌표값이 2이라면, 왼쪽 이동
                visited.append([i, j])
                if stk:
                    if stk[-1] != arr[i][j]:  # stk에 추가, 중복 제거
                        stk.append(arr[i][j])

                else:
                    stk.append(arr[i][j])

                j -= 1

            else: # 나머지(좌표값이 3)라면, 위쪽 이동
                visited.append([i, j])
                if stk:
                    if stk[-1] != arr[i][j]:  # stk에 추가, 중복 제거
                        stk.append(arr[i][j])

                else:
                    stk.append(arr[i][j])

                i -= 1


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = list(algorithm2(arr))
    print(f"#{test_case}", *ans)