#Do not change the line of code below. It's at the top of
#the file to ensure that it runs before any of your code.
#You will be able to access french_dict from inside your
#function.
french_dict = {"me": "moi", "hello": "bonjour",
               "goodbye": "au revoir", "cat": "chat",
               "dog": "chien", "and": "et"}




#Write your function here!
def french2eng(sentence):
    sentence = sentence.lower()
    sentence = sentence.split()
    # This method return a French value for the given key. If key is not available, then returns default       value of word.
    return ' '.join(str(french_dict.get(word, word)) for word in sentence)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
print(french2eng("Hello it's me"))