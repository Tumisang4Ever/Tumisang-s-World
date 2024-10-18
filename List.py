# Take input from the user for the number of elements they want to add to the list
n = int(input("Enter the number of elements: "))
  
l1 = list() # Initialize an empty list to store the elements
for i in range(n): # Loop to take 'n' number of inputs from the user
    ele = int(input("Enter the number: ")) # Take input for each element and convert it to an integer
    l1.append(ele)  # Append the integer element to the list 'l1'
    
s = sum(l1)   # Calculate the sum of all elements in the list
Min = min(l1) # Find the minimum value in the list
Max = max(l1) # Find the maximum value in the list
avg = s /  len(l1) # Calculate the average of the list by dividing the sum by the length of the list

# Print the results
print ("Sum of numbers is: ", s)
print ("Minimum element is: ", Min)
print ("Maximum element is: ", Max)
print ("Average is: ", avg)