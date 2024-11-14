#Q.1) Write a Python program to print lowercase and uppercase alphabets of a string

# Define a string
text = "HelloWorld"

# Print lowercase alphabets
lowercase = [char for char in text if char.islower()]
print("Lowercase letters:", lowercase)

# Print uppercase alphabets
uppercase = [char for char in text if char.isupper()]
print("Uppercase letters:", uppercase)


Output:
Lowercase letters: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
Uppercase letters: ['H', 'W']