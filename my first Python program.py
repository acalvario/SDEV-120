print("Hello World")
print("I just wrote my first Python Program")
print("This is so much fun")

#Here is a comment that can document my code.

name = input("Hello, what is your name?")  #gets the user's name
print("Welcome, it is so nice to meet you " + name) #prints a message with the user's name

"""

Simple script that constructs and prints the sentence:
    "It is raining cats and dogs."

Variables:
    c (str): first plural noun (no punctuation) -> "cats"
    d (str): second plural noun (no punctuation) -> "dogs"
    s (str): the sentence to print; assembled from c and d
"""

# Set variables (documented and typed)
c: str = "cats"    # first noun, do NOT include punctuation here
d: str = "dogs"    # second noun, do NOT include punctuation here

# Build the sentence with correct spacing and final period
s: str = f"It is raining {c} and {d}."

# Optional internal check (placed BEFORE the required final print)
# This asserts the sentence is exactly what the assignment expects.
assert s == "It is raining cats and dogs.", f"Unexpected output: {s}"

# The last command must be print(s)
print(s)
