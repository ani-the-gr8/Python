
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

