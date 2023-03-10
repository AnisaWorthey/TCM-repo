#Booleans and Operators 

valid = True
not_valid = False

print(valid)
print(type(valid))
print(not_valid)
print(type(not_valid))

print (valid == True) #valid is equal to True = True 
print(not_valid == True) #not_valid is equal to False = False 

print(valid != True) #Valid does not equal true
print(not_valid != True) #not valid does not equal true

print(not valid) # Not true = False 
print(not not_valid) # Not false = True

print ("--------------------------------------------------------------------------------")

print((10 < 9 ) == True) #Check to see if 10 less than 9 is == True = False
print((10 == 10) == True) #To see if 10 is == to 10 = True
print((10 != 10) == True)# To seee if 10 does not == 10 = False
print((10 >= 10) == True) # To see if 10 is greater than or equal to 10 = True 
print((10 <= 10) == True)
print((10 > 10) == True)

print ("--------------------------------------------------------------------------------")

print(10 > 5 and 10 < 5) # Is 10 greater than 5 AND is 10 less than 5 = False
print (10 > 5 or 10 < 5) # is 10 greater than 5 OR is 10 less than 5 = True

print(bool(0)) # Zero = Falae
print(bool(1)) # One = True

print(bool(0) == False) #zero(false) is equal to false = True
print(bool(1) == True) # One(True) is equal to true = True

print ("--------------------------------------------------------------------------------")
print ("--------------------------------------------------------------------------------")

print (10 + 10) # = 20
print (10 -10) #0
print (round(100/3)) #33 (without round 33.3333)
print (10//10) #1