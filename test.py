def add(a, b):
    # TODO: add input validation
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b

result = add(10, 5)
print(result)
total = divide(20, 4)
print(total)
product = multiply(4, 5)
print(product)
