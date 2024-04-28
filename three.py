A, B, C = map(int, input().split())

if A > B:
    if A > C:
        print("A is greater")
    else:
        print("C is greater")
elif B > C:
    print("B is greater")
else:
    print("C is greater")

