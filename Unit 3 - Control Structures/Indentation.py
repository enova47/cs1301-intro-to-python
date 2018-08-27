mystery_value = 1

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#All of the indentation has been removed from this program.
#Fix the program by correcting the indentation levels. Note
#that you should add indentation by adding FOUR SPACES to the
#start of the lines you want to indent. If you use Tab, you
#will receive an IndentationError in your output.
#
#Hint: you'll learn more about conditionals in the next
#chapter, but for now, all you need to know is that if a line
#is indented under another line, it's controlled by that line.

if mystery_value > 0:
    print("This line should only run if 'mystery_value' is GREATER than 0.")
    print("This line should only be printed if the above line is printed.")
print("This line should always be printed.")
if 0 > mystery_value:
    print("This line should only run if 'mystery_value' is LESS than 0.")
print("This line should always be printed.\n")