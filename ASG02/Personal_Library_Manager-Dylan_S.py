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

def main():
    display_menu()

if __name__ == "__main__":
    main()
