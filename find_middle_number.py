a = int(input())
b = int(input())
c = int(input())
print("ur numbers: ", a, b, c)

if a > b > c or a < b < c:
    int(print(b, "middle number"))
else:
    if b > a > c or b < a < c:
        int(print(a, "middle number"))
    else:
        int(print(c, "middle number"))
