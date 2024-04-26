def reverse_integer(number):
    # Check if the number is negative
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    
    # Initialize a variable to store the reversed number
    reversed_number = 0
    
    # Reverse the number using modulo and integer division
    while number != 0:
        # Extract the last digit of the number
        last_digit = number % 10
        # Append the last digit to the reversed number
        reversed_number = (reversed_number * 10) + last_digit
        # Remove the last digit from the original number
        number = number // 10
    
    # If the original number was negative, make the reversed number negative
    if is_negative:
        reversed_number = -reversed_number
    
    return reversed_number

# Example usage
number = 12345
reversed_number = reverse_integer(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
