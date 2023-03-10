# Conditonal statments

if True:
    print("True")
    
if False:
    print("False")
    
if not False:
    print("not False")

print("-------------------------------------------------------------------------------------")

# If-elif-else: "else 1"

if (1 < 1 ):
    print("Too big: False")
elif 1 <= 0:
    print ("Too big: False")
    print ("Here")
else: 
    print ("else 1")
    
print("-------------------------------------------------------------------------------------")

# IF-elif-else-boolean-conditional: "Else Reached"

if 1 > 1:
    print ("1 < 1") # 
elif 1 <=1:
    print ("1 <= 1")
elif 2<= 2:
    print("2 <= 2 ")
else:
    print("else reached")
    
print("-------------------------------------------------------------------------------------")

# If-Boolean-Conditional 

if 1 > 0 and 0 < 1: print ("1 > 0 and 0 < 1")
    
if 1 < 0 and 0 < 1: print ("1 < 0 and 0 < 1")
    
if (1 < 0 or 0 < 1) and 1 == 1: print("1 < 0 or 0 < 1")

# One of the two options in the "()" must be true AND one must equal one
print("-------------------------------------------------------------------------------------")

# Shorthand 

if 0 < 1: print ("0 < 1")
print ("1 >= 1") if 1 >= 1 else print ("1 < 1")