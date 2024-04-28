# Read an integer input from the user
N = int(input())

# Check if N is divisible by both 5 and 11
if N % 5 == 0 and N % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

# Check if N is divisible by 5
if N % 5 == 0:
    print("Divisible by 5")

# Check if N is divisible by 11
if N % 11 == 0:
    print("Divisible by 11")

