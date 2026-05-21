def c_to_f(celcious_temp):
    return (celcious_temp * 9/5) + 32

def f_to_c(fahrenheit_temp):
    return(fahrenheit_temp - 32) * 5/9

temp = input("Convert to (c/f): ")

if temp == "c":
    f_temp = float(input("Enter the Temperature in Fahrenheit: "))
    result = f_to_c(f_temp)
    print (f"The temperature in celcious: {result}")

elif temp == "f":
    c_temp = float(input("Enter the Temperature in celcious: "))
    result = c_to_f(c_temp)
    print(f"The temperature in fahrenhiet: {result}")