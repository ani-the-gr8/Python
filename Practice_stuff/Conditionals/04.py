num_1= float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
operator = input("Choose the operator { +  -  *  /}: ")

if operator == "+":
    print (f"Additon: {num_1 + num_2}")
elif operator == "-":
    print (f"Difference: {num_1 - num_2}")
elif operator == "*":
    print (f"Product: {num_1 * num_2}")
elif operator == "/":
    print (f"Division: {num_1 / num_2}")
else:
    print ("Choose a valid operator")
    