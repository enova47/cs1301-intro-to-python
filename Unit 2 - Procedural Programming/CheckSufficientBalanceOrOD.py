balance = 20.0
price = 19.0
overdraft_protection = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Last exercise, we printed True if balance was greater than or
#equal to price, and False otherwise. However, some banks have
#something called overdraft protection. Overdraft protection
#means that the customer is allowed to spend more than their
#balance, and the bank just expects them to deposit the money
#to cover the purchase later.
#
#Write some code below that will print True if the customer
#can make the purchase given their balance, the purchase
#price, and whether or not they have overdraft protection.
#Specifically, the result should be True if balance is greater
#than or equal to price or if overdraft_protection is True,
#and False if neither of these are true.


#Add your code here!
def balance_checker(balance1, price1, op1):
    if balance1 >= price1 or op1 == True:
        return True
    else:
        return False
print(balance_checker(balance, price, overdraft_protection))