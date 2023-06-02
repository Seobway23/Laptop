import sys
sys.stdin = open('input.txt')

# gear direction
def gear_dir(g, dir_g):
    Dir = [0, 0, 0, 0]
    Dir[g-1] = dir_g
    for i in range(4):
        num = (g+i+4)//4
        if Dir[num]==0:
            # 0일 떄
            if num == 0:
                if gear[0][2] == gear[1][6]:
                    Dir[num] = - ((g+i+4-1)//4)
                else:
                    Dir[num] = ((g+i+4-1)//4)
            # 3일 때
            elif num == 3:
                if gear[2][2] == gear[3][6]:
                    Dir[num] = -((g+i+4-1)//4)
                else:
                    Dir[num] = ((g+i+4-1)//4)
            # 1, 2 일 때
            elif num == 1:
                if gear[0][2] == gear[1][6]:
                    Dir[num] = - ((g+i+4-1)//4)

                else:
                    Dir[num] = ((g + i + 4 - 1) // 4)

                if gear[1][2] == gear[2][6]:
                    Dir[num] = - ((g+i+4-1)//4)
                else:
                    Dir[num] = ((g+i+4-1)//4)

            elif num == 2:
                if gear[1][2] == gear[2][6]:
                    Dir[num] = - ((g + i + 4 - 1) // 4)

                else:
                    Dir[num] = ((g + i + 4 - 1) // 4)

                if gear[2][2] == gear[3][6]:
                    Dir[num] = - ((g + i + 4 - 1) // 4)
                else:
                    Dir[num] = ((g + i + 4 - 1) // 4)
    return Dir


def gear_move(i, direction):
    ans_lst = [0]*8
    if direction == 1:
        for j in range(8):
            Index = (j + 1)//8
            ans_lst[i] = gear[i][Index]
    else:
        for j in range(8):
            Index = (8 + j - 1)//8
            ans_lst[j] = gear[i][Index]





gear = [list(map(int, input())) for _ in range(4)]
N = int(input())
ans = 0
for _ in range(N):
    g, dir_g = map(int, input().split())
    Dir = gear_dir(g, dir_g)

    for i in range(4):
        gear_move(i, Dir[i])

        if gear[i][0] == 1:
            print(i, gear[i][0])
            ans += i + 1
print(ans)