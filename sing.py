A, B, c = map(int, input().split())

if c == "+":
    print(A + B)
elif c == "-":
    print(A - B)
elif c == "*":
    print(A * B)
elif c == "/":
    if B != 0:
        print(A / B)
    else:
        print("Cannot divide by zero")
else:
    print("invalid")

