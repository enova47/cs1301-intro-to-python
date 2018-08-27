mystery_state = "Georgia"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#It's snowing!
#
#The variable above holds the name of the state that you're
#in (hypothetically). Complete the code below so that it
#prints the following messages depending on what state you're
#in:
#
# - "School isn't cancelled." if we're in New Jersey
# - "School is postponed." if we're in North Carolina
# - "School is cancelled!" if we're in Georgia
# - "idk wear a sweater" if we're in any other state (or if
#   the value doesn't represent a valid state).


#Add your code here!
if mystery_state == "New Jersey":
    print("School isn't cancelled.")
elif mystery_state == "North Carolina":
    print("School is postponed.")
elif mystery_state == "Georgia":
    print("School is cancelled!")