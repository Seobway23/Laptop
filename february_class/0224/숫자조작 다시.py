import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    target = list(input())

    # mn, mx 설정
    strnum= ''
    for t in target:
        strnum += t
    mn = int(strnum); mx = int(strnum);

    i = 0 # 바꾸기 설정
    for i in range(len(target)): # len(target)-1 까지 움직임
        for j in range(i+1, len(target)):
            #deepcopy
            deepcopy = []
            for k in target:
                deepcopy.append(k)
            deepcopy[i], deepcopy[j] = deepcopy[j], deepcopy[i]

            # 0 예외처리
            if deepcopy[0] == '0':
                #i += 1 애초에 이거는 하면 안됨
                continue

            #str 만들기
            str1 = ''
            for b in deepcopy:
                str1 += b

            a = int(str1)

            #mn, mx 갱신
            if mn > a:
                mn = a

            if mx < a:
                mx = a


    print(f"#{test_case} {mn} {mx}")









