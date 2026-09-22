"""Part of the picture of the code. These are the different options the user can do in their personal library manager.
main() is needed for later after more of the code is added to execute all steps of the code."""


def display_menu():
    print("\n========== Personal Library Manager =========")
    print("Please select an option:")
    print("1. Add a book title")
    print("2. Remove a book")
    print("3. List all book titles")
    print("4. Search a book title")
    print("5. Save and Exit")


def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    year = input("Enter book year: ").strip()

    if not title or not author or not year:
        print("Error: title, author, and year cannot be blank.")
        return

    new_book = {'title': title.title(), 'author': author.title(), 'year': year}
    library.append(new_book)
    print(f"Approved! '{new_book['title']}' has been added to your library.")


def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the book title to remove: ").strip().title()

    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"'{title}' has been successfully removed.")
            return

    print(f"Error: '{title}' was not found in the library.")

def book_list(library):
    if not library:
        print("The library has no books listed.")
        return

    print(" --- Current Book Inventory --- ")
    for index, book in enumerate(library, start=1):
        print(f"{index}. '{book['title']}' by {book['author']} and published in {book['year']}")


def search_list(library, title=None, author=None, year=None):
    """Search books by title, author, and/or year."""
    if title is None:
        title = input("Enter title to search (leave blank to skip): ").strip()
    if author is None:
        author = input("Enter author to search (leave blank to skip): ").strip()
    if year is None:
        year = input("Enter year to search (leave blank to skip): ").strip()

    results = []
    t = title.lower().strip() if title else None
    a = author.lower().strip() if author else None
    y = year.lower().strip() if year else None

    for book in library:
        book_title = str(book.get('title', ''))
        book_author = str(book.get('author', ''))
        book_year = str(book.get('year', ''))

        match = True
        if t and t not in book_title.lower():
            match = False
        if a and a not in book_author.lower():
            match = False
        if y and y != book_year:
            match = False

        if (t or a or y) and match:
            results.append(book)

    if not results:
        print("No matching books found.")
        return results

    print("Search Results:")
    for index, book in enumerate(results, start=1):
        print(f"{index}. '{book['title']}' by {book['author']} and published in {book['year']}")

    return results


def end_and_exit():
    print("Exiting Program... Have a nice day now!")
    raise SystemExit
"""Added the end_and_exit() function for the user
to end the program and exit it. Raising the sysem exit will terminate the program 
and return control to the operating system."""


def main():
    library = []
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
            search_list(library)
        elif choice == "5":
            end_and_exit()
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()

