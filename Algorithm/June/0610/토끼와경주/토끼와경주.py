import sys
sys.stdin = open('input.txt')

'''
N * M 격자
pi di(이동해야하는 거리)
처음 토끼는 1행 1렬에 있음

경주 진행
가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것 K번 반복
    # 우선순위
    PQ=sorted(총 점프횟수, 행+렬 작은 번호, 행번호, 열 번호, 고유번호)
    PQ.popleft() -> i번째 토끼
    
    for 상하좌우
        di 만큼 이동했을 때 위치 구함
        격자 벗어나면 방향을 반대로 바꿔 한칸 이동 -> 점화식 세워야 함
    
    R_move_list=sorted(행+열, 행, 열, reverse=True)
    A = R_move_list.popleft()
    for i번째 토끼를 제외한 모든 토끼 
        i제외 모든 토끼 ++ A[0] ++ A[1]

    점수 합계S
    C = sorted(행 + 열, 행, 열, 고유번호, reverse=True)
    S += C[0]

한번이라도 뽑혔는지
visited 배열 -> 토끼의 고유번호 부여

'''


def move(pri_R, distance, idx, di, dj):
    ni, nj = pri_R[2], pri_R[3]
    for _ in range(distance):
        # print('ni:',ni, 'nj:',nj, 'di:',di[idx], 'dj:',dj[idx])
        ni, nj = ni + di[idx], nj + dj[idx]

        if ni > N or ni < 0 or nj > M or nj < 0:
            idx = (idx + 2) % 4
            ni, nj = ni + di[idx], nj + dj[idx]
    return ni, nj


def race(K, S, R_info):
    # Count, i+j, i, j, id, distance, Score
    R_info = sorted(R_info, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
    pri_R = R_info[0]

    # 4방향 MOVE
    di, dj = [-1, 0, 1, 0], [0, -1, 0, 1]
    next_list = [[] for _ in range(4)]
    for i in range(4):
        ni, nj = move(pri_R, pri_R[5], i, di, dj)
        # print('ni:', ni, 'nj:', nj)

        # 움직일 때, 격자를 벗어 나게 되면 방향을 반대로 바꿈
        next_list[i] = [ni+nj, ni, nj]

    next_list = sorted(next_list, key=lambda x: (x[0], x[1], x[2]), reverse=True)
    # print('next_list:',next_list , 'next_list[0][0]:', next_list[0][0])
    for rabbit in R_info:
        # 이동 하지 않은 토끼 score update
        # id : 4, score: 6
        if rabbit[4] != pri_R[4]:
            rabbit[6] += next_list[0][0]

        # 이동한 토끼 info update
        if rabbit[4] == pri_R[4]:
            # Count, i+j, i, j, id, distance, Score
            rabbit[0] += 1                  # count 더하기
            rabbit[1] += next_list[0][0]    # i + j 더하기
            rabbit[2] += next_list[0][1]    # i 더하기
            rabbit[3] += next_list[0][2]    # j 더하기
            rabbit[7] = 1
    # print(' 토끼 정보들:', R_info)
    # visited 적기
    if not pri_R[7]:
        visited[visited_num][0] = pri_R[4]
        visited[visited_num][1] = 1
    return

# 초기값
visited = []
visited_num = 0
# N 행, M 열, P 토끼_리스트
N, M, P = 0, 0, 0
pid = []
# Count, i+j, i, j, id, distance, Score, visited
R_info = []

n = int(input())
for _ in range(n):
    commend, *arr = map(int, input().split())

    if commend == 100:
        # 방문 유무에 따른 토끼 리스트
        # id, 방문 여부
        # 정보 update
        N, M, P = arr[0], arr[1], arr[2]
        visited = [[0, 0] for _ in range(P)]
        # print('visited:', visited)
        pid = arr[3:]

        # Count, i+j, i, j, id, distance, Score
        R_info = [[0]*8 for _ in range(P)]

        # Rabbit_정보 갱신
        for i in range(P):
            # id , distance update
            R_info[i][4], R_info[i][5] = pid[2*i], pid[2*i +1]

    if commend == 200:
        K, S = arr[0], arr[1]
        for _ in range(K):
            race(K, S, R_info)
            visited_num += 1

        # Third Sort: 우선 순위가 높은 토끼 += S
        # i+j : 2, i :3, j : 4, id: 5 reverse= True
        R_info = sorted(R_info, key=lambda x: (x[2], x[3], x[4], x[5]), reverse=True)
        # score : 6
        R_info[0][6] += S

    # 토끼의 이동 거리 변경
    if commend == 300:
        modify_id = arr[0]
        modify_dist = arr[1]
        # id: 4,  distance: 5
        for Ri in R_info:
            if Ri[4] == modify_id:
                Ri[5] = modify_dist

    if commend == 400:
        R_info = sorted(R_info, key=lambda x: (x[6]), reverse=True)
        print(R_info[0][6])

