
# Python Exercises Set 3 Question 3: Median of Three Values
# Sample answer / tutorial (Colin Simon-Fellowes)

# Question Text:
# Write a function that takes three numbers as parameters, and
# returns the median value of those parameters as its result.
# include a main program that reads three values from the user
# and displays their median.


#               --- CODED SOLUTION ---               #


# Basic function to get the median of three values (the middle value)
# Purposefully expanded to give insight into the steps taking place

def get_median_basic_logic(a,b,c):

    max_num = max([a,b,c])                      # Gets the biggest number of the three
    min_num = min([a,b,c])                      # Gets the smallest number of the three

    for num in [a,b,c]:                         # Goes over each of the three numbers
        if num != max_num and num != min_num:   # If a number is neither the biggest or smallest (middle), outputs that number and ends
            return num

# A different and more compact version that simply sorts the three numbers and outputs the one in the middle
# Again, expanded for clarity

def get_median_basic(a,b,c):

    sorted_nums = sorted([a,b,c])
    middle_num = sorted_nums[1]     # recall that the index of a 3-element list is [0, 1, 2], so the middle element is at index 1

    return middle_num

# Fully compacted
def get_median(a,b,c):
    return sorted([a,b,c])[1]

# A main function to get 3 integer values from the user and display a message with the median value
# Note that the restriction to integers is simply arbitrary and can be changed

def main():

    num_1 = int(input("First Number: "))        # Get first number and convert to int
    num_2 = int(input("Second Number: "))       # Get second number and convert to int
    num_3 = int(input("Third Number: "))        # Get third number and convert to int

    median = get_median(num_1, num_2, num_3)    # Pass to our function and get the median
    print("Median Number:",median)              # Display the median


if __name__ == "__main__": main()               # Ensures that our main function only runs when we call it (not when this file is imported by another program)


# Extra Credit (useful skills to learn):
# 
# - rewrite main so it takes only one input of three numbers separated by commas (and maybe spaces) and breaks it into three integer variables
#   - Useful things to research are python's functions split() and strip(), as well as tuple unpacking
# 
# - rewrite get_median so it takes one input in the form of a list of arbitrary size and flexibly finds the median
#   - Consider how the index of the middle element of a 3-element list is 1. what would this index be for a 4-element list? 5?
#   - Research how medians are found. In a list of even length, how does one determine the middle element?
#   - Python's len() function and the modulo (%) operator could be useful for determining whether the length of a list is even or odd