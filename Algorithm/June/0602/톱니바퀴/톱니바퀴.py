'''
톱니가 움직이지 못하는 경우를 생각하지 못함
그래서 많은 시간을 할애함
1. 구조화시켜 구현할 수 있는 행동, 함수를 구현한 후
체계적으로 풀 것
'''


import sys
from collections import deque
sys.stdin = open('input.txt')


def check_right(g, direction):
    global Dir
    if g > 3 or gear[g-1][2] == gear[g][6]:
        return

    if gear[g-1][2] != gear[g][6]:
        # 돌릴 때 움직이려면 방향이 반대여야 함
        check_right(g + 1, -direction)
        # 돌린다음에 체크
        gear[g].rotate(direction)


def check_left(g, direction):
    global Dir
    if g < 0 or gear[g][2] == gear[g+1][6]:
        return

    if gear[g][2] != gear[g+1][6]:
        check_left(g - 1, -direction)
        gear[g].rotate(direction)


gear = [deque(list(map(int, input()))) for _ in range(4)]
N = int(input())

# dir 체크
for _ in range(N):
    G, direction = map(int, input().split())
    g = G-1
    check_right(g+1, -direction)
    check_left(g-1, -direction)
    # 돌린다음에 체크하면 안되니까 돌리기전에 체크, 그리고 마지막에 돌리기
    gear[g].rotate(direction)

ans = 0
for i in range(4):
    # print(gear[i])
    if gear[i][0] == 1:
        ans += 2**i
print(ans)

#
# # gear direction
# def gear_dir(g, dir_g):
#     Dir = [0, 0, 0, 0]
#     Dir[g-1] = dir_g
#     for i in range(4):
#         num = (g+i+4) % 4
#         print('g:', g, 'i:', i, 'num:', num)
#         if Dir[num] == 0:
#             # 0일 떄
#             if num == 0:
#                 if gear[0][2] == gear[1][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#             # 3일 때
#             elif num == 3:
#                 if gear[2][2] == gear[3][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#             # 1, 2 일 때
#             elif num == 1:
#                 if gear[0][2] == gear[1][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#
#                 if gear[1][2] == gear[2][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#
#             elif num == 2:
#                 if gear[1][2] == gear[2][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#
#                 if gear[2][2] == gear[3][6]:
#                     Dir[num] = Dir[(4+num-1)%4]
#                 else:
#                     Dir[num] = -Dir[(4+num-1)%4]
#     return Dir
#
#
# def gear_move(i, direction):
#     ans_lst = [0]*8
#     if direction == 1:
#         for j in range(8):
#             Index = (j + 1) % 8
#             ans_lst[i] = gear[i][Index]
#     else:
#         for j in range(8):
#             Index = (8 + j - 1) % 8
#             ans_lst[j] = gear[i][Index]
#     gear[i] = ans_lst
#
#
#
#
#
# gear = [list(map(int, input())) for _ in range(4)]
# N = int(input())
# ans = 0
# for _ in range(N):
#     g, dir_g = map(int, input().split())
#     Dir = gear_dir(g, dir_g)
#     print(Dir)
#
#     for i in range(4):
#         gear_move(i, Dir[i])
#         print('i:', i, f"gear[{i}][0]:", gear[i][0])
#
#         if gear[i][0] == 1:
#             # print('i:', i, f"gear[{i}][0]:", gear[i][0])
#             ans += i + 1
# print(ans)