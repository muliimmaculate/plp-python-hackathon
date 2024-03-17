def fibonacci(n):
 
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get user input for the number of terms
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = [fibonacci(i) for i in range(n)]

# Print the generated Fibonacci sequence
print("The number of terms in the fibonacci_sequence is:", (fibonacci_sequence))
