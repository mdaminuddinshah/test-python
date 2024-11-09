item = 'orange'
Item = 'apple'
ITEM = 'grape'

print(f"{item} is great")
print('{} is good' .format(ITEM))
print('%s is nice' % Item)

# PRINT WITH f-strings (f"{var}")
exit = 'amin'
EXIT = 12

# the EXIT and exit will be string, using f-strings the variable automatically become string
print(f"his name is {exit} and he is {EXIT}")


# PRINT WITH .format -> ("{} .format()")
good = 'shah'
GOOD = 12

print("his name is {} and he is {}" .format(good, GOOD))

# PRINT WITH COMMAS 
kind = 'hanim'
KIND = 12 

print("her name is", kind, "and", KIND)

# PRINT WITH CONCATENATION
nice = 'farida'
NICE = 12

print("she " + nice + " really great " + "person " + "and is she " + str(NICE))


