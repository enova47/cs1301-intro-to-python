mood = "impatient"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#We've written some code below that prints out what kind of
#tea we want to  buy based on our mood. The code has an error,
#though. Rewrite the code so that it runs with the correct
#output.
#
#The correct output if mood is one of the expected moods
#(sad, anxious, tired) is the name of the tea and the cost.
#The correct output if mood is not one of the expected moods
#is None and "free".
#
#Hint: this is a scope problem!

if mood == "sad":
    tea = "oolong"
    cost = 3.99
elif mood == "anxious":
    tea = "green tea"
    cost = 5.45
elif mood == "tired":
    tea = "english breakfast"
    cost = 4.35
else:
    tea = None
    cost = "free"

print(tea)
print(cost)