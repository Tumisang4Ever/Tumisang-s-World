# Take input from the user, asking for a number (n) to calculate its factorial
n = int(input("Enter any number: "))

# Initialize a variable 'f' to store the factorial result, starting with 1
f = 1

# Loop from 'n' down to 1 (inclusive) to calculate the factorial
# The range function generates numbers from 'n' to 1 (decrementing by 1)
for i in range(n, 0, -1):
    # Multiply the current value of 'f' by 'i' to accumulate the factorial product
    f *= i

# Print the final factorial value
print("Factorial is", f)
