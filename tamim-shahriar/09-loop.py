"""
def multiple_with_function(n):
    print(n, "x 1 =", n * 1)
    print(n, "x 2 =", n * 2)
    print(n, "x 3 =", n * 3)
    print(n, "x 4 =", n * 4)
    print(n, "x 5 =", n * 5)
    print(n, "x 6 =", n * 6)
    print(n, "x 7 =", n * 7)
    print(n, "x 8 =", n * 8)
    print(n, "x 9 =", n * 9)
    print(n, "x 10 =", n * 10)
    
n = input("Please enter a number: ")
n = int(n)

for i in range(1, n+1):
    multiple_with_function(i)
    print("")
   """
    
    # while_loop for py
    
i = 1
    
while i <= 10:
        print(i)
        i = i + 1
        
# calculate multplication with while loop

def multplication_table(n):
    for i in range(1, 11):
        print(" {} X {} = {}".format(n, i, n * i))
        
n = input("Enter a number (0 to exit) :")
n = int(n)

while n != 0:
    multplication_table(n)
    print("")
    n = input("Enter a number (0 to exit): ")
    n = int(n)