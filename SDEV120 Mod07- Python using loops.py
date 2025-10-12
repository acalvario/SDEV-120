# Program to check if numbers in a list are even or odd and sum
# Author: [Ana Calvario]
# Date: [October 07, 2025]

# - Part A: Sum of user-entered numbers -
print("Enter numbers to add them up. Emter 0 to stop.")

total = 0 # variable to hold the running sum

while True:
    user_input = int(input("Enter a number (0 to stop): "))
    if user_input == 0:
        break
    total += user_input

print("The sum of the numbers you entered is::", total)

# - Part B: Even/Odd check on a list -
print("\nNow analyzing a list of 15 numbers...")

# Define a list of 15 numbers
number_list = [2, 5, 6, 10, 13, 15, 18, 20, 1, 11, 4, 30, 50, 40, 60]

# Loop through the list and check even or odd
for number in number_list :
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

