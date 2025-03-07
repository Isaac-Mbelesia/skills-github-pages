# Function to reverse a range of numbers
def reverse_range(start, end):
    # Create a list of numbers in the specified range
    numbers = list(range(start, end + 1))
    # Reverse the list
    reversed_numbers = numbers[::-1]
    return reversed_numbers

# Get the starting digit from the user
start_digit = int(input("Enter the starting digit: "))
# Get the ending digit from the user
end_digit = int(input("Enter the ending digit: "))

# Call the function and store the result
result = reverse_range(start_digit, end_digit)

# Print the reversed list of numbers
print("Reversed numbers:", result)
