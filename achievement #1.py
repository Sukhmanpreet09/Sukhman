#geometry calculator
#1 Calculate the area of a circle
#2 calculate the area of a rectangle
#3 calculate the area of a triangle
#4 quit

#enter the choice(1-4)
choose= int(input("choose the number from (1-4)"))
if choose == 1:
    r=int(input("enter the radius of the circle in cm :"))# choose the radius of the circle in cm
    print("the area of the circle in cm^2: ", (3.14*(r*r) ))# area of the circle in cm^2
    print("the perimeter of the circle in cm :", (2*3.14*(r*r)))#perimeter of the circle in cm
elif choose==2 or choose == 3:
    l=(int(input("length of the rectangle/triangle in cm: ")))#choose the length for the rectangle/triangle in cm
    w=(int(input("width of the rectangle/triangle in cm: ")))#choose the width for the rectangle/triangle in cm
    print("the area of the rectangle/triangle in cm :", l*w)#area of the rectangle/triangle in cm^2
    print("the perimeter of the rectangle/triangle :", 2*(l+w))#perimeter of the rectangle/triangle in cm
elif choose==4:
    print("Quit")


