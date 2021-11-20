
# Python Exercises Set 3 Question 1: Shipping Cost
# Sample answer / tutorial (Colin Simon-Fellowes)

# Question Text:
# An online retailer provides express shipping for many of their items at a rate
# of €10.95 for the first item and €2.95 for each successive item. Write a function
# that takes the number of items in the order as its only parameter. Return the
# shipping charge for the order as the function's result. Include a main program
# that reads the number of items purchased from the user and displays the shipping charge


#               --- CODED SOLUTION ---               #


# Function to calculate shipping cost
# Expanded to show in detail each step

def get_cost_basic(items):

    initial_charge = 8                              # If we reword the question, what is actually charged is a €8 flat fee and €2.95 for every item
    total_charge = initial_charge + 2.95 * items    # as ( 10.95 + 2.95*(items-1) ) == ( 8 + 2.95 + 2.95(items-1) ) == ( 8 + 2.95*(items) )
    
    return total_charge

# Or, more concisely
def get_cost(items):
    return 8 + 2.95 * items

# Main function to read # items from the user and return she shipping charge

def main():
    num_items = int(input("Number of Items: "))     # Note that the inputted number of items is necessarily an integer, as fractional items are not a thing
    shipping_cost = get_cost(num_items)             # Passes the number of items to our function to get the shipping cost

    print("Shipping cost:",shipping_cost)           # Displays a message with the shipping cost for the inputted number of items

if __name__ == "__main__":                          # Ensures that our main function only runs when we call it (not when this file is imported by another program)
    main()

# Extra Credit (useful skills to learn):
# 
# - Edit the print statement in main so that it properly formats the shipping cost to look like an amount of money.
#   - This includes: commas separating every three digits, two decimal places (even for whole-euro amounts), and a proper currency symbol
#   - When properly done this would convert a raw example output of 501800 (int) to "€501,800.00" (str)
#   - For a starting point look up python3 currency formatting, and try to learn about each of the different components that make up the format
# 
# - If the user enters a value which is illegal (a float, letters, spaces, etc.), alert them with a message and then ask them to enter another value.
#   - learn about 'while' loops in Python, the Python isdigit() function, (potentially) try-except statements