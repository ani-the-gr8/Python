def uppercase():
    my_str = 'hello world'
    uppercase_my_str = my_str.upper()
    print(uppercase_my_str)  # HELLO WORLD

def lowercase ():
    my_str = 'Hello World'
    lowercase_my_str = my_str.lower()
    print(lowercase_my_str)  # hello world

def strip ():
    my_str = '  hello world  '
    trimmed_my_str = my_str.strip()
    print(trimmed_my_str)  # "hello world"

def sting_replace():
    my_str = 'hello world'
    replaced_my_str = my_str.replace('hello', 'hi')
    print(replaced_my_str)  # hi world

def split():
    my_str = 'hello world'
    split_words = my_str.split()
    print(split_words)  # ['hello', 'world']

def join():
    my_list = ['hello', 'world']
    joined_my_str = ' '.join(my_list)
    print(joined_my_str)  # hello world

def startswith ():
    my_str = 'hello world'
    starts_with_hello = my_str.startswith('hello')
    print(starts_with_hello)  # True

def endswith():
    my_str = 'hello world'
    ends_with_world = my_str.endswith('world')
    print(ends_with_world)  # True

def find_keyword():
    my_str = 'hello world'
    world_index = my_str.find('world')
    print(world_index)  # 6

def count():
    my_str = 'hello world'
    o_count = my_str.count('o')
    print(o_count)  # 2

def capitalize():
    my_str = 'hello world'
    capitalized_my_str = my_str.capitalize()
    print(capitalized_my_str)  # Hello world

def is_upper():
    my_str = 'hello world'
    is_all_upper = my_str.isupper()
    print(is_all_upper)  # False

def is_lower():
    my_str = 'hello world'
    is_all_lower = my_str.islower()
    print(is_all_lower)  # True

def title():
    my_str = 'hello world'
    title_case_my_str = my_str.title()
    print(title_case_my_str)  # Hello World










