def bigger_num(a,b,c):
    if a > b and a>c:
        print (f"{a} is greater than {b} and {c}")
    elif b >a and b > c:
        print (f"{b} is greater than {a} and {c}")
    elif c > a and c > b:
        print (f"{c} is greater than {a} and {b}")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

bigger_num(a, b, c)