
# This is a header block example for lab 2.
# You will need to supply the following information.

# Name:
# Section:

# Create a welcome message
# Input: a name as a string
# Result: a string
def welcome_message(name : str) -> str:
   message = "Hello, " + name + "."
   return message

message = welcome_message("jpreci05@calpoly.edu")
print (message)

def concat_string(string1 : str, string2 : str) -> str:
   return string1 + string2
concat_string("hello", "world")