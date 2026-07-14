marks = input ("Enter your marks: ")

marks = int(marks)

if marks >= 80:
    print("GPA: A")
elif marks >= 70: 
    print("GPA: B")
elif marks >= 60: 
    print("GPA: C")
elif marks >= 50: 
    print("GPA: D")
else: 
    print("GPA: F")

print("✅ Done")


# Boolean type conditional logic handle

a = 4

a == a # true

a == 4 # true

a == 3 # false

a != 3 # true

# Conditional login even and odd number calculation

n = input("Enter your number")
n = int(n)

# Uses and && or 
if n >= 0 and n % 2: 
    print (n, "is positive and even number")
elif n >=0 and n % 2 == 1: 
    print(n, "is positive and odd number")
elif n < 0 and n % 2 == 0 : 
    print(n, "is negative and odd number")

if n >= 0 or n % 2: 
    print (n, "is positive and even number")
elif n >=0 or n % 2 == 1: 
    print(n, "is positive and odd number")
elif n < 0 or n % 2 == 0 : 
    print(n, "is negative and odd number")
