def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    
    for digit_str in num_str:
        digit = int(digit_str)
        total += digit ** num_digits
    
    return total == number

try:
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

