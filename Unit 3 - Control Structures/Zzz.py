mystery_string = "zizazzle"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The variable above creates a string. Add some code below
#that will print based on the maximum number of consecutive
#z's in the string:
#
# - If z appears three or more times in a row, print "I'm sleepy..."
# - If z appears two times in a row, print "I love ZZ Top!"
# - If z appears once, print "One is the loneliest number."
# - If z does not appear, print "Who needs z anyway?"
#
#The message you print should correspond to the most
#consecutive z's: in the original value of mystery_string,
#for example, you'd print "I love ZZ Top!" because there are
#two consecutive z's, even though there are also some
#individual z's.
#
#Ignore upper-case z's -- only look for lower-case z's.
#
#Hint: Remember the 'in' operator! It returns true if the
#first string is found within the second string. For example,
#"bog" in "boggle" would return True, but "bog" in "artemis"
#would return False.


#Add your code here!
if "zzz" in mystery_string:
    print("I'm sleepy...")
elif "zz" in mystery_string:
    print("I love ZZ Top!")
elif "z" in mystery_string:
    print("One is the loneliest number.")
elif "z" not in mystery_string:
    print("Who needs z anyway?")