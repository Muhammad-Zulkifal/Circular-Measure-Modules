import math
pi=math.pi

def Arc_Length():
    r=float(input("Enter Radius: "))
    O=float(input("Enter Angle: "))
    print("Arc Length is: ",r*O)

def Sector_Area():
    r=float(input("Enter Radius: "))
    O=float(input("Enter Angle: "))
    print("Sector Area is: ",(pow(r,2)*O)/2)

def Sector_Perimeter():
    r=float(input("Enter Radius: "))
    O=float(input("Enter Angle: "))
    print("Sector Perimeter is: ",((r*2)+ r*O))

def Segment_Area():
    r=float(input("Enter Radius: "))
    O=float(input("Enter Angle: "))
    print("Segment Area is: ",((pow(r,2)*(O-math.sin(O)))/2))

def Segment_Perimeter():
    r=float(input("Enter Radius: "))
    O=float(input("Enter Angle: "))
    S=pow(2*(pow(r,2)*(1-math.cos(O))),1/2)
    print("Segment Perimeter is: ",((O*r)+S))

def Angle1():
    Area=float(input("Enter Area: "))
    r=float(input("Enter Radius: "))
    print("Angle is: ",((2*Area)/pow(r,2)))

def Angle2():
    r=float(input("Enter Radius: "))
    Arc=float(input("Enter Arc Length: "))
    print("Angle is: ",(Arc/r))

def Radius1():
    Area=float(input("Enter Area: "))
    O=float(input("Enter Angle: "))
    print("The radius is: ",pow((2*Area)/O,1/2))

def Radius2():
    Arc=float(input("Enter Arc Length: "))
    O=float(input("Enter Angle: "))
    print("The radius is: ",(Arc/O))

def Angle_Radius():
    Arc=float(input("Enter Arc Length: "))
    Area=float(input("Enter Area: "))
    r=2*(Area/Arc)
    O=Arc/r
    print("Radius: ",r,"Angle: ",O)
count=1
while count<=5:
    print("Solve for?")
    print("1. Arc Length")
    print("2. Sector Area")
    print("3. Sector Perimeter")
    print("4. Segment Area")
    print("5. Segment Perimeter")
    print("6. Angle (Area Given)")
    print("7. Angle (Arc Length Given)")
    print("8. Radius (Area Given)")
    print("9. Radius (Arc Length Given)")
    print("10. Angle and Radius")
    x=int(input("Enter a Number from the list: "))
    if x==1:
        Arc_Length()
    elif x==2:
        Sector_Area()
    elif x==3:
        Sector_Perimeter()
    elif x==4:
        Segment_Area()
    elif x==5:
        Segment_Perimeter()
    elif x==6:
        Angle1()
    elif x==7:
        Angle2()
    elif x==8:
        Radius1()
    elif x==9:
        Radius2()
    elif x==10:
        Angle_Radius()
    count=count+1
            
    

    
