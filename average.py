# Initialize count and total to 0
count = 0
total = 0

# Read the first value
value = float(input("Enter your number (enter 0 to stop): "))

# While the entered value is not 0
while value != 0:
    # Add the value to the total
    total = total + value
    
    # Increase the count of how many values were entered
    count = count + 1

    # Read the next value
    value = float(input("Enter your number: "))

# Display error and end the loop by entering 0
if count == 0:
    print("No values entered.")
else:
    # Compute the average and display the result
    average = total / count
    print("Average is = ", average)
