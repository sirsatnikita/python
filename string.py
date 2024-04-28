'''nik = input("Enter the string :- ")
nik = nik.lower()
for i in range(97,123):
    count = 0
    j = chr(i)
    for l in nik :;
        if j==l:
            count+=1
    if count > 0:
        print(j,":",count)
my_string = "hello world"'''

'''string1 = "Hello"
string2 = "World!"
n = 8

result = string1[:n] + string2[:n - len(string1)]
print(result)'''

'''string1 = "nikita"
string2 = "sirsat"
if string1 == string2:
    print("equal")
else:
    print("not equal")
if string1 < string2:
    print("befor")
else:
    print("after")'''

'''string = "nikitasirsat "
print(len(string))'''

'''string = "nikitasirsat"
revers = string[::-1]
print(revers)'''

'''n = "nikita! how are you, 123"
vowel = 0
constanant = 0
digit = 0
space = 0
for char in n:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowel+=1
        else:
            constanant+=1
    elif char.isdigit():
        digit+=1
    elif char.isspace():
        space+=1
print(vowel)
print(constanant)
print(digit)
print(space)'''
'''string1 = "nikita sirsat"
string2 = string1[:]
print(string2)
string1 = "nikita"
string2 = "sirsat"
string3 = string1,string2
print(string3,end="")'''
# Source string
'''source_string = "Hello, World!"

# Initialize an empty string for the destination
destination_string = ""

# Copying source string to destination string
for char in source_string:
    destination_string += char

# Displaying the copied strings
print("Source string:", source_string)
print("Copied string:", destination_string)'''
'''string = "12371"
revers = string[::-1]
if string == revers :
    print("palindrom")
else:
    print("not palindrom")'''

'''input_string = "abccbaacz"
seen = {}
for i, char in enumerate(input_string):
    if char in seen:
        print(f"Output for '{input_string}': {char}")
        break
    seen[char] = idx'''
'''string_input = "nikita sirsat"
sorted_string = ''.join(sorted(string_input))
print(string_input)
print(sorted_string)'''
'''string_input = "nikita sirsat"
lower_string = string_input.lower()
upper_string = string_input.upper()
print(lower_string)
print(upper_string)'''
'''r= "nikita sirsat"
first = r[-1]
print(first)'''
'''total_days = 500

# 1 year = 365 days
years = total_days // 365
remaining_days = total_days % 365

# 1 week = 7 days
weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(f"{total_days} days is approximately {years} years, {weeks} weeks, and {remaining_days} days.")'''
sub1 = float(input("Enter the sub :- "))
sub2 = float(input("Enter the sub :- "))
sub3 = float(input("Enter the sub :- "))
sub4 = float(input("Enter the sub :- "))
sub5 = float(input("Enter the sub :- "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
varage = total_marks/5
total_marks_of_all = 500
percentag = (total_marks / total_marks_of_all)*100
print(total_marks )
print(varage)
print(percentag)



