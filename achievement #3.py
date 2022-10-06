#input length checker

#enter user' name



name=input("enter your name")
isUpper = False
isNumber = False
if len(name)<=1:
    print("Sorry, username must be longer than one letter.")
elif len(name)>=20:
    print( "Sorry, username cannot be more than 20 letters in length.")
else:
    for x in name:
         if (x.isdigit()):
            isNumber = True
            
         if(x.isupper()):
            isUpper = True  
       

if(isUpper == False and isNumber == False):
   print( "Sorry, Please re enter name.") 
else:
    print("done!")


