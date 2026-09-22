def find_max(numbers):
    return max(numbers)

# Create an empty list
nums = []

# Take 5 numbers as input and add them to the list
for i in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)

# Call the function and print the result
print("The maximum number is:", find_max(nums))