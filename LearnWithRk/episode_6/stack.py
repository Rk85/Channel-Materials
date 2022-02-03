my_string = input("Please give string only with { or } to validate: ")

my_list = list(my_string)
my_stack = []

for cur_char in my_list:
    if cur_char == '{':
        my_stack.append(cur_char)
    elif cur_char == '}':
        previous_char = None
        if my_stack:
            previous_char = my_stack.pop()
        if previous_char != '{':
            print("Not closed properly")
            break
else:
    print("Properly closed")
    
