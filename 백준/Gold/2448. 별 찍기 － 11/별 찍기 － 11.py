def fractal(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    prev = fractal(n // 2)
    top_1 = [ " " * (n // 2) + line +" " * (n // 2) for line in prev]
    bottom_2 = [line + " " + line for line in prev]
    return top_1 + bottom_2


n = int(input())
arr = fractal(n)
print("\n".join(arr))
