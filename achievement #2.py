#geometry calculator using function
#1 Calculate the area of a square
#2 calculate the area of a rectangle
#3 calculate the area of a circle
#4 quit
#enter the choice(1-4)
value = input("choose the number from (1-4)")
choose= int(value.strip())

def circle():
    r=int(input("enter the radius of the circle in cm :"))# choose the radius of the circle in cm
    print("the area of the circle in cm^2: ", (3.14*(r*r) ))# area of the circle in cm^2
    print("the perimeter of the circle in cm :", (2*3.14*(r*r)))#perimeter of the circle in cm
def rectangle():
    l=(int(input("length of the rectangle in cm: ")))#choose the length for the rectangle in cm
    w=(int(input("width of the rectangle in cm: ")))#choose the width for the rectangle in cm
    print("the area of the rectangle/triangle in cm :", l*w)#area of the rectangle in cm^2
    print("the perimeter of the rectangle/triangle :", 2*(l+w))#perimeter of the rectangle/triangle in cm
def square():
    a=int(input("enter the side of the square in cm: "))#enter the length of the side of the square in cm
    print("the area of square in cm^2 :", a*a)
    print("the perimetr of the square in cm: " , 4*a)
if choose == 3:
    circle()
elif choose==2:
    rectangle()
   
elif choose==1:
    square()
 
elif choose==4:
    print("Quit")





