#print function: Prints stuff
print ("Hi")

var = "Data in a variable"
print (var)

# Type function: Shows the type of a data.

print (type("hi"))
print (type("71"))
print (type(71))
print (type(71.1))
print (type(True))
print (type(False))

#Isinstance function: Checks the type of the given data and return a bool value.
print (isinstance("hi", str)) #True
print (isinstance(71, int)) #True
print (isinstance(71.1, float)) #True
print (isinstance(True, bool)) #True

print (isinstance("hi", int)) #False
print (isinstance(71, str)) #False
print (isinstance(71.1, int)) #False
print (isinstance(True, float)) #False


