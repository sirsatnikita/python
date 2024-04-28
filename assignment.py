#Write a Python program to determine whether a given year is a leap year or not.

'''def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
year=int(input("enter the num"))
if is_leap_year(year):
    print(year,"this is leap year")
else:
    print(year,"this is not leap year")'''

# Create an if-elif-else block to determine the grade based on a student’s score 
# (e.g., A for 90-100, B for 80-89, etc.).
    
'''gread=int(input())
if gread>90 and gread<100:
    print("A gread")
elif gread >80 and gread<90:
    print("B") 
elif gread >70 and gread<80:
    print("C")
elif gread >60 and gread<70:
    print("D")
else:
    print("fail")'''

#Generate the first n prime numbers using a while loop.
'''n=int(input("enter the num :- "))
c=0
i=1
while i<=n:
    if n % i ==0 :
        c+=1
        i+=1
if c==2:
    print("prime")
else:
    print("not prime")'''

#Calculate the sum of all even numbers from 1 to 100 using a for loop.
# def is_even(numbers):
#     sum_evevn=0
#     for i in range(1,numbers):
#         if i%2==0:
#             sum_evevn+=i
#     return sum_evevn
# num=int(input("enter number:- "))
# result=is_even(num)
# print(result)

#Write a Python function that takes a list of integers as input and returns the product of all positive numbers in the list.


# def positive(nums):
#     product = 1
#     for num in nums:
#         if num > 0:
#             product *= num
#     return product

# n = list(map(int, input("Enter the list of numbers separated by space: ").split()))
# pro = positive(n)
# print(pro)

#Create a list of fruits and print each fruit in reverse order.


# mylist = ["apple", "banana","orange","charry"]
# revers = [elem[::-1] for elem in mylist]
# print(revers)

# Define a tuple containing the names of three programming languages. Print each language name along with its length.

# names = ("html", "c++", "css", "Python")
# for name in names:
#     language = len(name)
#     print(name, language)

#Create a Python function that checks if two sets are disjoint (i.e., have no common elements).

# def are_disjoint(set1,set2):
#     return set1.isdisjoint(set2)

# set1={2,4,6,7}
# set2={3,5,2,4}
# print(are_disjoint(set1,set2))
#Find the union of two sets containing integers from 1 to 10 and 5 to 15.

# set1=set(range(1,11))
# set2=set(range(5,16))

# union_set=set1.union(set2)
# print(union_set)


#Create a dictionary representing a book with keys for title, author, and publication year.
# book= {
#     "title":"gutghut",
#     "author":"nikita",
#     "publication":"2023"
# }
# print(book)
#Write a function that takes a list of numbers and returns the maximum value.

# n=[4,6,2,4,7,9]
# print(max(n))

#Create a Python program that reads an integer from the user. Handle any invalid input (e.g., non-integer values) by displaying an appropriate error message.
# try:
#     user_input=int(input("enter an initeger:-"))
#     print("you entered",user_input)
# except ValueError:
#     print("Error: please enter a valid integer.")
# def Zero():
#     a=int(input())
#     b=int(input())
#     if b==0:
#         raise ZeroDivisionError
#     return a/b
# print(Zero())


#19.Write a Python function that takes two sets as input and returns their intersection (common elements).
# def intersection(set1,set2):
#     return set1.intersection(set2)
# set1={1,3,5,6,7}
# set2={4,6,8,9,2}
# result=intersection(set1,set2)
# print(result)

#Define two variables and swap their values using tuple unpacking.
# m=23
# t=27
# m,t=t,m
# print(m)
# print(t)



# def fab(n):
#     a = 0
#     b = 1
#     while a < n:
#         print(a)
#         a, b = b, a + b

# n = int(input("Enter the limit for Fibonacci sequence: "))
# fab(n)

# def character(str):
#     vowels=['a','e','i','o','u']
#     if str in vowels:
#         return "vowels"
#     else:
#         return "consonant"
# con=input("enter the charactere:-")
# result=character(con)
# print(result)

# n=int(input("enter the num"))
# i=1
# f=1
# while i<=n:
#     f=f*i
#     i+=1
# else:
#     print(f)
# Write a Python program that checks if a given string is a palindrome (reads the same backward as forward).

# n=str(input("enter the str"))
# k=''.join(reversed(n))
# if n==k:
#     print("palindrom")
# else:
#     print("not palindrom")

# def duplicat(lst):
#     uniqe=[]
#     for i in (lst):
#         if i not in uniqe:
#             uniqe.append(i)
#     return uniqe

# input=input("enter the elements : -" )
# result=(input)
# print(result)

# def remove_duplicates(input_list):
#     return list(set(input_list))

# # Example usage:
# input_list = [1, 2, 3, 4, 2, 3, 5]
# result = remove_duplicates(input_list)
# print("List after removing duplicates:", result)

# Create a list of squares of numbers from 1 to 10 using list comprehension

# square=[x**2 for x in range(1,11)]
# print(square)


# def occurrence(elements):
#     counts={}
#     for i in elements:
#         if i in counts:
#             counts[i]+=1
#         else:
#             counts[i]=1
#     return counts
# element = int(input("enter the array"))
#elements=element.split()
# print(occurrence(element))

# def intersection(list1,list2):
#     new=[]
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 new.append(i)
#     return new
# output=[2,4,6,8]
# output2=[4,8,1,6]
# print(intersection(output,output2))

# n=input("enter the strinig")
# m=input("enter the 2 string")
# if len(n)==len(m):
#     is_anagram=True
#     for i in range(len(n)):
#         if n[i] not in m:
#             is_anagram=False
#             break
#     if is_anagram:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("no")
# def Myfunction(str):
#     for i in range(str):
#         if i in str:
#             counts=+1
#             k=counts,str(i)
#         else:
#             counts=1
#             k=counts,str(i)
#     return str
# output=input("enter the str")
# print(output)

# def unique(s):
#     char_count={}
#     for char in s:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     for i in range(len(s)):
#         if char_count[s[i]]==1:
#             return s[i]
#     return Nond
# def sort_tuple(arr):
#     sorted_tuple=sorted(arr,key=lambda x:x[1])
#     return sorted_tuple
# input_tuple= [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# print(sort_tuple(input_tuple))
# def duplicat(arr):
#     duplicats=set()
#     for i in arr:
#         if arr.count(i)>1:
#             duplicats.add(i)
#     return duplicats
# output=[1,2,3,1,2,3,4]
# print(duplicat(output))

# Printing the first 5 even numbers
# for i in range(2, 12, 2):
#     print(i)

# # Printing pyramid of asterisks
# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()

# for i in range(2, 12, 2):
#     print(i)
#rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()

