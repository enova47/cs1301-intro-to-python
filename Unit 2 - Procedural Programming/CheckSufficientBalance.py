balance = 20.0
price = 19.0

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine we're writing some software for a cash register or
#credit card processor. We want to approve a purchase if the
#customer's balance is greater than the purchase price, and
#reject it otherwise.
#
#Write some code below that will print True if balance is
#greater than or equal to price, and False if it is not.


#Add your code here!
def balance_checker(balance1, price1):
    if balance1 >= price1:
        return True
    else:
        return False

print(balance_checker(balance, price))