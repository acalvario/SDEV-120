# Program to check if numbers in a list are even or odd
# Author: [Your Name]
# Date: [Today's Date]
#List of 15 numbers
numbers = [2, 5, 6, 10, 13, 15, 18, 20, 1, 11, 4, 30, 50, 40, 60]
# Loop through the list and check even or odd
for number in numbers:
    if number % 2 ==0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
