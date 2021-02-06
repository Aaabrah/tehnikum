a = int(input())
b = int(input())
c = int(input())
print("find among", a, b, "and", c, "largest number")

if a > b > c:
    print(a, "is the largest number")
else:
    if b > a > c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")
