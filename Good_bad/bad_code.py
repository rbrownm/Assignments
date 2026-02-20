def calculate_add(x, y):
    result = 0
    numbers = [x, y]
    for num in numbers:
        result += num
    return result

def calculate_subtract(x, y):
    result = 0
    answer = [x - y]

    return answer[0]

def calculate_multiply(x, y):
    result = 0
    numbers = [x, y]

    for num in numbers:
        result = x * y

    return result

def run():

    calculate_log = []
    time_to_run = 0

    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    time_to_run = time_to_run + 1

    add = str(calculate_add(x, y))
    subtract = str(calculate_subtract(x, y))
    multiply = str(calculate_multiply(x, y))

    print("Add: " + add)
    print("Subtract: " + subtract)
    print("Multiply: " + multiply)

run()

