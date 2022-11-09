def function1(a, b):
    print("Hello you are in function1 and the sum of a and b is", a + b)


def function2(a, b):
    """This is a function which will calculate average of two numbers"""
    average = (a + b) / 2
    return average


v = function2(9, 6)
print(v)
print(function2.__doc__)
