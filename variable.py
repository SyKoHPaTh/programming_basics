''' Introduction to Programming Basics

	Make for a Youtube Tutorial video.

	Programming Basics Playlist: https://www.youtube.com/playlist?list=PLBaS0R4eUcBe54RYKoeBuzZuXxnWd9JNs

    License:  Free for Public/Personal/Commercial Use

    Author: SyKoHPaTh

    Shameful Self-Promotion:
        - Discord   https://discord.gg/UeNKDCJ
        - Website   http://www.sykohpath.com

    If you have any question/comments/concerns/kittens, please ask on the Discord!
'''

variable_integer = 5000

variable_boolean = False # Boolean True = 1, False = 0

variable_string = 'Bob'

#Base 10 = 0 through 9

#int() 		# Explicitly define it as an Integer
#float()		# Explicitly define it as an Float
#string()	# Explicitly define it as an String

#print( type(variable_string) )
#print( variable_string )

# Basic Math!

# + operator: Amazing, and can do many things!
var_x = variable_integer + 50
var_x = variable_string + 'ob'

# - operator; not as amazing and magical as +
var_x = variable_integer - 50

# * operation; multiplies!
var_x = variable_integer * variable_string

# / operator; is it amazing?
variable_int_two = 3 # this is definitely an integer!
var_x = int(variable_integer / variable_int_two)

# % operator; deals with remainders
var_x = variable_integer % variable_int_two

# ** operator; power of!
var_x = 2 ** 3

# // operator; answer is int()
var_x = variable_integer // variable_int_two
# // the same as: int(variable_integer / variable_int_two)

print(var_x)