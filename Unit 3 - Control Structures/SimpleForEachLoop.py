mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "abc", the output would be:
#0 a
#1 b
#2 c
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.


#Add your code here!
letters = 0

for character in mystery_string:
    print(str(letters) + " " + character)
    letters += 1