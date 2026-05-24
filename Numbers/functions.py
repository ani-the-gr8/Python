def round_function():
    #round function: Rounds the number to a specific place.
    #Syntax: round (float, place till which to round)
    float_1 = 9.2342
    float_2 = 13.9485

    round_1 = round(float_1)
    round_2 = round(float_2 , 2)

    print (round_1)
    print(round_2)

def absolute_value():
    #Returns the absolute value from the 0 in a number line.
    num = -12
    abs_val = abs(num)
    print (abs_val)

def power_function():
    result_1 = pow(2, 3) #Equivalent to 2 **3
    print (result_1) #8

    result_2 = pow(2, 3, 5) # Equivalent to (2**3) % 5
    print (result_2) #3

