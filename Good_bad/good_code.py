def calculate_add(x, y):
    return x + y

def calculate_subtract(x, y):
    return x - y

def calculate_multiply(x, y):
    return x * y

def run():
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))

    print(calculate_add(x, y))
    print(calculate_subtract(x, y))
    print(calculate_multiply(x, y))


run()