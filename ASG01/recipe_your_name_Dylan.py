"""
Recipe Card CLI Program

Course:     IST 242
Term:       Fall '26
Assignment #: ASG01
Assignment Name: Recipe Card CLI
Author:     [Dylan Smith]
Date:       [09/07/26]

This program runs in the command line and allows the user to enter
basic information about a recipe. While running the program, the user
will be prompted to:

1. Enter a recipe name
2. Enter ingredients (one at a time)
   - Type 'Q' to stop entering ingredients ("quit")
3. Enter a positive, non-zero cooking time (in minutes)

After all input is collected, the program displays the combined
recipe information in a readable, numbered format.
"""


def prompt_for_recipe_name():
    """Returns the recipe name entered by the user."""
    return input("Please enter a recipe name: ")


#------------------------------------------------------------
def prompt_for_ingredients():
    """Prompts the user to enter ingredients until they type Q."""
    ingredients_list = []
    while True:
        ingredients = input("Enter ingredients (type Q to quit): ")
        if ingredients.upper() == "Q":
            break
        if ingredients.strip() == "":
            continue
        ingredients_list.append(ingredients)
    return ingredients_list
"""When Q is entered, 
the loop will end to then return the list of ingredients typed in by the user."""
#-------------------------------------------------------------
def prompt_for_cooking_time():
    """Prompts the user to enter a valid cooking time."""
    while True:
        try:
            cooking_time = float(input("Please enter a cooking time in minutes: "))
            if cooking_time > 0:
                return cooking_time
        except ValueError:
            pass
        print("Please enter a positive, non-zero cooking time.")
"""The user can only enter a number that is not below zero or negative for the 
cooking time because it will return as ValueError if the case."""
#--------------------------------------------------------------
def combine_info(recipe_name, ingredients, cooking_time):
    """
    Combines recipe information into a single formatted string.
    """
    output = f"Recipe: {recipe_name} (cooking time = {cooking_time})\n"
    for number, ingredient in enumerate(ingredients, start=1):
        output += f"{number}. {ingredient}\n"
    return output.rstrip()


def main():
    """Main function that controls the flow of the program."""
    recipe_name = prompt_for_recipe_name()
    ingredients = prompt_for_ingredients()
    cooking_time = prompt_for_cooking_time()
    final_recipe = combine_info(recipe_name, ingredients, cooking_time)
    print(final_recipe)


# This ensures the program runs only when this file is executed directly
if __name__ == "__main__":
    main()
