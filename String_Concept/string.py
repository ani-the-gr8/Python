
def opposite_quote_use():
    #Using Opposite quotes to close the statement, when using single + double quote combo
    msg = "It's a sunny day"
    quote = 'She says, "Hello World!"'
    print (quote)
    print (msg)

def escape_quotation_with_backslash():
    #Backslash (\) ignores the very next quotation mark.
    msg = 'It\'s a sunny day'
    quote = "She said, \"Hello!\""
    print (msg)
    print (quote)

def in_operator():
    my_str = 'Hello world'
    print('Hello' in my_str)  # True
    print ("hello" in my_str)  #False
    print('hey' in my_str)    # False
    print('hi' in my_str)    # False
    print('e' in my_str)  # True
    print('f' in my_str)  # False
    print (" " in my_str)  #True

def length_function():
    #Shows the length of the characters in a string.
    my_str = 'Hello world'
    print(len(my_str))

def indexing():
    #String Indexing: Shows the residence of an alphabet through index numbers.
    my_str = "Hello world"
    print(my_str[0])  # H
    print(my_str[6])  # w
    print(my_str[-1])  # d
    print(my_str[-2]) # l

def string_concatenation():
    my_str_1 = 'Hello'
    my_str_2 = "World"

    str_plus_str = my_str_1 + " " + my_str_2
    print(str_plus_str) # Hello World

def typecasting():
    name = 'John Doe'
    age = 26

    name_and_age = name + str(age)
    print(name_and_age) # John Doe26

def augmented_assignment_operator():
    name = 'John Doe'
    age = 26

    name_and_age = name  # Start with the name
    name_and_age += str(age)  # Append the age as string
    print(name_and_age)  # John Doe26

def string_interpolation():
    name = 'John Doe'
    age = 26
    name_and_age = f'My name is {name} and I am {age} years old'
    print(name_and_age) # My name is John Doe and I am 26 years old

def string_interpolation_2():
    num1 = 5
    num2 = 10
    print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
    

