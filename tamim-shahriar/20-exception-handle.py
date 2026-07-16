while True:
    n1 = int(input("Please enter a number: "))
    n2 = int(input("Please enter a another number: "))
    
    if n1 == 0 and n2 == 0:
        break
    try:
        print("Result of devision\n", n1/n2)
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print("Good work!")