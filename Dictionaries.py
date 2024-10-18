contact = {} # Initialize an empty dictionary to store contacts


def display_contact(): # Function to display all contacts in the dictionary
    print("Name\t\tContact Number") # Print header
    
    # Iterate through the dictionary and print each contact's name and phone number
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

# Infinite loop to keep the program running until the user chooses to exit
while True:
    
    # Display a menu of choices for the user and take input
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3.Display contact\n 4. Edit contact \n 5. Delete contact\n 6.Exit\n Enter your choice "))
    
    if choice == 1: # Option 1: Add a new contact
        
        # Take input for the contact name and phone number
        name = input("enter the contact name ")
        phone = input("enter the mobile number")
        
         # Add the new contact to the dictionary with name as key and phone as value
        contact[name] = phone
        
    # Option 2: Search for an existing contact    
    elif choice == 2:
        
        # Take input for the contact name to search
        search_name = input("enter the contact name ")
        
        if search_name in contact:  # Check if the name exists in the dictionary
            
            # If found, print the contact number
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            
            # If not found, inform the user that the contact doesn't exist
            print("Name is not found in contact book")
    
     # Option 3: Display all contacts
    elif  choice == 3:
        
        if not contact: # If the contact list is empty, inform the user
            print("empty contact book")
        else:  
            
            # Otherwise, call the display_contact() function to show all contacts
             display_contact()    
    
    # Option 4: Edit an existing contact
    elif  choice == 4:
        
        # Take input for the name of the contact to be edited
        edit_contact = input("Enter the contact to be edited ")
        
        if edit_contact in contact: # Check if the contact exists in the dictionary
            
            phone = input("enter mobile number") # Take input for the new phone number
            contact[edit_contact]=phone  # Update the contact with the new phone number
            print("contact updated")  
            
            display_contact()   # Display updated contact list 
        else:
            
            # If contact doesn't exist, inform the user
            print("Name is not found in contact book")
            
    # Option 5: Delete an existing contact        
    elif choice == 5:
        
        # Take input for the name of the contact to be deleted
        del_contact = input("Enter the contact to be deleted ")
        
        if del_contact in contact:   # Check if the contact exists in the dictionary
            
            # Confirm if the user wants to delete the contact
            confirm = input("Do you want to delete this contact y/n? ")
            
            if confirm =='y' or confirm =='Y': # If confirmed, delete the contact from the dictionary
                contact.pop(del_contact)
                
            display_contact()   # Display the updated contact list
        else:
            
            # If contact doesn't exist, inform the user
            print("Name is not found in contact book")
            
    else:  # Option 6: Exit the program 
        break   # Break out of the loop and terminate the program
                                      