def fractal(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    next_num = n // 2
    prev = fractal(next_num)
    # top은 next_num 만큼 빈칸을 양 옆으로 띄워주면 됨
    top = [" " * (next_num) + line +  " " * (next_num)  for line in prev]
    # bottom은 line 과 line 사이에 " " 공백 하나만 있으면 됨
    bottom = [line + " " + line for line in prev]
    return top + bottom


n = int(input())
arr = fractal(n)
print("\n".join(arr))