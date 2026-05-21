def simple_interest(p, r, t):
    print (f"Simple Interetst: {p * r * t / 100}")

p = float(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

simple_interest(p, r, t)