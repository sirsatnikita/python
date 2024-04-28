n = int(input())
x = 10
arr = list(map(int,input().split()))
found = 0
for i in range(n):
    if arr[i] == x:
        print(x)
        found = 1
        break

if found==0:
    print("not found")

