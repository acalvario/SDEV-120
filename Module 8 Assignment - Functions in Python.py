# user-defined function called square accepting one variable that is stored in x
def square (x):
    y= x*x
    return y

result = square(10)
print(result)

# Function definition
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

#First test:a = 2, b = 3
a = 2
b = 3
result = greater_than(a, b)

#Print result
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Second test: a = 10, b = 6
a = 10
b = 6
result = greater_than(a, b)

#Print result
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
