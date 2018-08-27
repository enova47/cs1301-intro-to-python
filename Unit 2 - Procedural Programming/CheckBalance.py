balance = 20.0
price = 19.0
sales_tax_rate = 1.06

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Remember last chapter when we were writing a little program
#to check if a person has enough money in their account to
#make a certain purchase. At the time, we just checked their
#balance, the price, and possibly overdraft protection.
#
#Now, let's add sales tax. To find the actual purchase cost,
#we need to multiply the price by the sales tax rate.
#
#Write some code below that will print True if balance is
#big enough to make a purchase with the given price and sales
#tax rate, False if it is not.


#Add your code here!
actual_cost = balance > (price * sales_tax_rate)
print(actual_cost)