from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# [0] : i, [1]: j, [2]: number
houses = []
chickens =[]
h_num, chk_num = 1, 1
hq = []
cur_chk = set()

# 1,2 리스트 담기
def find_house_chickens():
    global h_num, chk_num
    for i in range(n):
        for j in range(n):
            # 집 이면
            if arr[i][j] == 1:
                houses.append((i, j, h_num))
                h_num += 1

            if arr[i][j] == 2:
                chickens.append((i, j, chk_num))
                chk_num += 1

    # print("1: ", houses)
    # print("2: ", chickens)
    return


# 여기 까지가, 각 집 당 우선 순위 선택한 것
#------------
# def make_pq():
#     for hi, hj, h_num in houses:
#         tmp_hq = []
#         for chk_i, chk_j, chk_num in chickens:
#             heapq.heappush(tmp_hq, ((abs(hi - chk_i) + abs(hj - chk_j)), chk_num))
#         hq.append(tmp_hq)
#------------

def check_cur_chk():
    for k in range(len(hq)):
        cur_chk.add(hq[k][0][1])

    return len(cur_chk)

def ans():
    cnt = 0
    for k in range(len(hq)):
        cnt += hq[k][0][0]

    return cnt


def optimal():
    lst = [k for k in range(len(chickens))]
    perm_lst = combinations(lst, m)
    cons = float('inf')
    for lst in perm_lst:
        cnt = 0
        for hi, hj, h_num in houses:
            h_cnt = float('inf')
            for k in lst: # 가장 작은 거 찾기
                chk_i, chk_j, chk_num = chickens[k]
                dist = abs(hi - chk_i) + abs(hj - chk_j)
                h_cnt = min(h_cnt, dist)
            cnt += h_cnt

        # print(lst, cnt)
        cons = min(cons, cnt)

    print(cons)

# Main Process
find_house_chickens()
# make_pq()   #[0]: 거리, [1]: chk_num
chk_lst = check_cur_chk()
optimal()
