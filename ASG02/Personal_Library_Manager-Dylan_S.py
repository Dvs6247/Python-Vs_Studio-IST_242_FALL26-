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
    year = input("Enter book year: ").strip().title()
    #Comes up in the terminal to let the user type in the book information nicely
    library = []
    library.append(new_book)
    #Creates a place to store the book data and puts the book into the personal library list
    print(f"Approved! '{title}' has been added to your library.")
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

def book_list():
        for index, book in enumerate(book_list, start=1):
            print(" --- Current Book Inventory --- ")
            print (f"{index}. '{book['title']}' by {book['author']} and published in {book['year']}")
            """Added to the book_list function:
            added an index to be able to add books to the list
            and added a print command to show the text 'current book inventory' 
            with the book title, author, and year."""
        if not book_list:
             print("The library has no books listed.")
             return
"""Added to the book_list function: 
Added the command's output for if there are no books in the list"""

def search_list(book_list, title = None, author = None, year = None):
     results = []
     """Created a search_list function to find a specific book in the book list
     With the parameters of the search list accepting a, title, author, year typed in."""
     t = title.lower().strip() if title else None
     a = author.lower().strip() if author else None
     y = year.lower().strip() if year else None
     #Used to have a clean output of the title, author, and year.
     for book in book_list:
          book_title = str(book.get('title', ''))
          book_author = str(book.get('author', ''))
          book_year = str(book.get('year', ''))
          #Added the for function to how it lists the book's year, author, and title when requested.
          match = True
          if t and t not in book_title:
              match = False
          if a and a not in book_author:
              match = False
          if y and str(y) != book_year:
              match = False
          if (t or a or y) and match:
              results.append(book)
     return results
"""Added to search_list to match conditions for the title, author, and year
to then return these results once searched."""

def end_and_exit():
    print("Exiting Program... Have a nice day now!")
    exit()
"""Added the end_and_exit function and how the program ends and exits the user."""
        
        
def main():
    display_menu()
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            book_list(library)
        elif choice == "4":
            search_books(library)
        elif choice == "5":
            end_and_exit()
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
