
# Python Exercises Set 3 Question 6: What's the Hypoteneuse?
# Sample answer / tutorial (Colin Simon-Fellowes)

# Question Text:
# Write a function that takes the lengths of the two shorter sides of a right triangle as its
# parameters. Return the hypoteneuse of the triangle, computed using the Pythagorean Theorem,
# As the function's result. Include a main program which reads these two shorter lengths from
# The user, uses your function to compute the length of the hypoteneuse, and displays the result


#               --- CODED SOLUTION ---               #


# Function which takes two sides as parameters and returns hypoteneuse length
# Deliberately expanded to help with understanding of each step

def get_hypoteneuse_basic(a,b): 

    a_squared = a ** 2
    b_squared = b ** 2

    c_squared = a_squared + b_squared
    c = c_squared ** 0.5                                    # remember that (x ** 0.5) == (x ** (1/2)) == √x

    return c

# Or, more concisely:
def get_hypoteneuse(a,b):
    return ( a**2 + b**2 ) ** 0.5

# Main function to take user input for two legs and print the length of the hypoteneuse
# Note that in this function I decide to take integer (and not float) inputs, this is purely a design choice and can be changed

def main():
    side_a = int(input("Side A: "))                         # Get Side A, convert it to int
    side_b = int(input("Side B: "))                         # Get Side B, convert it to int

    hypoteneuse_length = get_hypoteneuse(side_a,side_b)     # Pass these to our function and store the result as a variable
    print("Hypoteneuse Length:", hypoteneuse_length)        # Display the length of the hypoteneuse to the user with a message


if __name__ == "__main__": main()                           # Ensures that our main function only runs when we call it (not when this file is imported by another program)

# Extra Credit (skills to learn):
#
# - Make a custom version of get_hypoteneuse that returns the value as an integer if it is a whole number, otherwise as a float
#   - The modulo (%) operator is a useful tool to determine whether a number is whole or not. Think about the remainder of a number divided by 1
# 
# - Make a custom version of main that takes only one input of two numbers separated by a comma (and maybe a space), and breaks them up into two variables
#   - Some useful things to research here are Python's strip() and split() functions, as well as the concept of tuple unpacking.