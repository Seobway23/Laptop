import sys
import math
from pprint import pprint
sys.stdin = open('input.txt')

# fish_list 함수
# 움직이면 갱신 -> 리스트 갱신 -> 샤크 갱신, 물고기 갱신 -> sort 갱신
# B = sorted(fish_list2, key=lambda x: (x[0], x[2], x[3]))

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)]

# fish_list 구하기

def arr_search():
    fish_list = [[] for _ in range(10)]
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                fish_list[arr[y][x]].append(y)
                fish_list[arr[y][x]].append(x)
    return fish_list


# 초기 값
fish_list = arr_search()

# shark 초기값
shark_size = 2
shark_y = fish_list[9][0]
shark_x = fish_list[9][1]

# 초기값
num = math.inf
dist = num
cx = num
cy = num
shark_eat = 0


# 정답 초기값
ans = 0

i = 1
while i < 9:
    if fish_list[i]:
        fish_lst2 = fish_list[i]
        fish_list2 = [[] for _ in range(len(fish_list[i])//2)]
        for j in range(0, len(fish_lst2), 2):
            dist = abs(fish_lst2[j]-shark_y) + abs(fish_lst2[j+1] - shark_x)
            # fish_list 추가 dist, y, x, idx
            fish_list2[j//2] += [dist, fish_lst2[j], fish_lst2[j+1]]

        fish_list3 = sorted(fish_list2, key=lambda x: (x[0], x[1], x[2]))
        q = fish_list3[0]
        print('dist:', dist, 'i:', i, 'fish_list3:' ,fish_list3, 'q:', q)

        # 계산
        dist = q[0]
        cy = q[1]
        cx = q[2]
        ans += dist
        shark_y = cy
        shark_x = cx
        shark_eat += 1
        # 갱신
        arr[cy][cx] = 0

        # pop
        print('fish_list[i]:',fish_list[i])
        fish_list[i].pop(0)
        fish_list[i].pop(0)

        if shark_size == shark_eat:
            shark_size += 1
            shark_eat = 0
            i += 1


    else:
        break


print(ans)