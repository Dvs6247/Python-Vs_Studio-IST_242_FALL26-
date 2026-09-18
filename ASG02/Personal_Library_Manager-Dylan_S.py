"""Part of the picture of the code. These are the different options the user can do in their personal library manager.
main() is needed for later after more of the code is added to execute all steps of the code."""
def display_menu():
    print("\n========== Personal Library Manager =========")
    print ("Please select an option:")
    print ("1. Add a book title")
    print ("2. Remove a book")
    print ("3. List all book titles")
    print ("4. Search a book title")
    print ("5. Save and Exit")

def add_book():
    #The user will use this option to add book details to their library
    new_book = {'title', 'author', 'year'}
    #Information the user types in for the information of the book
    title = input("Enter book title: ").strip().title()
    author = input("Enter book author: ").strip().title()
    year = input("Enter book author: ").strip().title()
    #Comes up in the terminal to let the user type in the book information nicely
    library = []
    library.append(new_book)
    #Creates a place to store the book data and puts the book into the personal library list
    print(f"Approved! '{title}' has been added to the library.")
    #prints out that the title has been added to the personal library

def remove_book(title, library):
    """Using the def function to
    use the 2nd option to remove a book using
    a book name/title that is from the library list"""
    if title in library:
        library.remove(title)
        #Added the if function to be able to remove a book's title from the library list
        print(f"'{title}' has been successfully removed.")
    else:
        print(f"Error: '{title}' was not found in the library.")
        """Added the print command to show on the terminal
        either the title does show the user successfully typed it correctly and removed it or
        with the else command that the title wasn't typed correctly to be removed."""
def remove_book(book_title, library_list):
    """Using the def function to
    use the 2nd option to remove a book using
    a book name/title that is from the library list"""
        


def main():
    display_menu()

if __name__ == "__main__":
    main()
