from calculator import add, sub, mul, div

a = int(input("Please provide the first value for addition: "))
b = int(input("Please provide the second value for addition: "))

operator = input("What do you want to do with these values(+,-, *, /) : ")

if operator == "+":
    print(add(a, b))
elif operator == "-":
    sub(a, b)
elif operator == "*":
    mul(a, b)
elif operator == "/":
    div(a, b)

