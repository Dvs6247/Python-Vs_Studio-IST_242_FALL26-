"""Part of the picture of the code. These are the different options the user can do in their personal library manager.
main() is needed for later after more of the code is added to execute all steps of the code."""
def display_menu():
    print("\n========== Personal Library Manager =========")
    print ("Please select an option:")
    print ("1. Add a book title")
    print ("2. Remove a book")
    print ("3. List all book titles")
    print ("4. Search a book title")
    print ("5. Exit")

def Add_book():
<<<<<<< HEAD
    #The user will use this option to add book details to their library
=======
    #The user will use this option to add book details to their library.
>>>>>>> 1669238b4f8f40cb37d9e40de00d3eae1aaefff6
    new_book = {'title', 'author', 'year'}
    #Information the user types in for the information of the book
    title = input("Enter book title: ").strip().title()
    author = input("Enter book author: ").strip().title()
    year = input("Enter book author: ").strip().title()
<<<<<<< HEAD
    #Comes up in the terminal to let the user type in the book information nicely
    library = []
    library.append(new_book)
    #Creates a place to store the book data and puts the book into the personal library list
    print(f"Approved! '{title}' has been added to the library.")
    #prints out that the title has been added to the personal library

#def Remove_book():

=======
    #Comes up in the terminal to let the user type in the book information nicely.
  
>>>>>>> 1669238b4f8f40cb37d9e40de00d3eae1aaefff6

def main():
    display_menu()

if __name__ == "__main__":
    main()
