z = 0
while True:
    print("Main Menu:- ")
    print("1. circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Cuboid")
    print("6. Cube")
    print("7. Cylinder")
    print("8. Cone")
    print("9. Sphere")
    print("10. Hemishere")

    ch = int(input("Choose Whats your shape: "))

    if ch==1 :
        while True:
            print("1. Area ")
            print("2. Length")
            print("3. Length of an arc ")
            print("4. area of sector")

            ch = int(input("Enter what you want to find: "))

            if ch==1:
                a = int(input("Enter the radius: "))
                b = 3.14*a*a
                print("Area of circle: ",b)

            elif ch==2:
                a = int(input("Enter the radius: "))
                b = 3.14*2*a
                print("Lenght of the circle: ", b)

            elif ch==3:
                a = int(input("Enter the radius: "))
                b = int(input("Enter the angle: "))
                c = (b/360)*2*3.14*a
                print("Lenght of an arc is ",c)

            elif ch==4:
                a = int(input("Enter the radius: "))
                b = int(input("Enter the angle: "))
                c = (b/360)*3.14*a*a
                print("Area of sector is ", c)

            else:
                print("Enter the valid statement. ")

    elif ch==2:
        a = int(input("Enter the Lenght: "))
        b = int(input("Enter the Breadth: "))
        c = a*b
        d = 2*(a+b)
        e = 0.5*(a*a)+(b*b)
        print("Area of the Rectangle: ",c)
        print("Perimeter of the Recantgle: ",d)
        print("Diagonal of the Rectangle: ", e)

    elif ch==3:
        a = int(input("Enter the side: "))
        print("Area of the Square: ", a*a)
        print("Perimeter of the Square: ", 4*a)
        print("diagonal of the Square: ", 1.41*a)

    elif ch==4:
        while True:
            print("1. Area of the triangle")
            print("2. Perimeter of the Triangle")
            print("3. Heron's Formula of the Triangle")

            ch = int(input("Enter the No. what you want to find: "))


            if ch==1 :
                a = int(input("Enter the value of Base: "))
                b = int(input("Enter the value of Height: "))
                print("Area of the Triangle: ", 0.5*a*b)

            if ch==2:
                a = int(input("Enter the value of the first side: "))
                b = int(input("Enter the value of second side: "))
                c = int(input("Enter the value of thrid side: "))
                print("Perimeter of the Triangle: ", a+b+c)

            if ch==3:
                a = int(input("Enter the value of the first side: "))
                b = int(input("Enter the value of second side: "))
                c = int(input("Enter the value of thrid side: "))
                s = (a+b+c)/2
                print("Area of triangle using Heron's Formula: ", 0.5*(s*(s-a)*(s-b)*(s-c)))

            else:
                print("Enter the vaild input.")

    elif ch==5:
        while True:
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            print("3. Volume of the Cuboid")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
                a = int(input("Enter the value of Lenght: "))
                b = int(input("Enter the value of Breadth: "))
                c = int(input("Enter the value of Height: "))
                print("Lateral Surface Area of Cuboid: ", 2*(a+b)*c)

            elif ch==2:
                a = int(input("Enter the value of Lenght: "))
                b = int(input("Enter the value of Breadth: "))
                c = int(input("Enter the value of Height: "))
                print("Total Surface Area of Cuboid: ", 2*(a*b)+(b*c)+(c*a))

            elif ch==3:
                a = int(input("Enter the value of Lenght: "))
                b = int(input("Enter the value of Breadth: "))
                c = int(input("Enter the value of Height: "))
                print("Volume of the Cuboid: ", a*b*c)

            else:
                print("Enter the correct value")

    elif ch==6:
        while True:
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            print("3. Volume of the Cube")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
              a = int(input("Enter the value of side: "))
              print("L.S.A of Cube: ", 4*a*a)

            elif ch==2:
                a = int(input("Enter the value of side: "))
                print("T.S.A of cube: ",6*a*a)

            elif ch==3:
                a = int(input("Enter the value of side: "))
                print("Volume of Cube: ", a*a*a)

            else:
                print("Entert the correct no. ")

    elif ch==7:
        while True:
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            print("3. Volume of the Cylinder")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                print("L.S.A of Cylinder: ",2*3.14*a*b)

            elif ch==2:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                print("T.S.A of Cylinder: ",2*3.14*a(b+a))

            elif ch==3:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                print("Volume of Cylinder: ", 3.14*a*a*b)

            else:
                print("Enter value Invalid, Try again")

    elif ch==8:
        while True:
            print("1. Lateral Surface Area")
            print("2. Total Surface Area")
            print("3. Volume of the Cone")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                c = 0.5*((b*b)+(a*a))
                print("L.S.A of Cone: ",3.14*a*c)

            elif ch==2:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                c = 0.5*((b*b)+(a*a))
                print("T.S.A of Cone: ", 3.14*a*(a+c))

            elif ch==3:
                a = int(input("Enter the Radius: "))
                b = int(input("Enter the Height: "))
                c = 0.5*((b*b)+(a*a))
                print("Volume of Cone: ", 1/3*3.14*a*a*b)

            else:
                print("Enter value invalid.")

    elif ch==9:
        while True:
            print("1. Lateral Surface Sphere")
            print("2. Total Surface Sphere")
            print("3. Volume of the Sphere")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
                a = int(input("Enter the Radius: "))
                print("L.S.A of Sphere: ", 4*3.14*a*a)

            elif ch==2:
                b = int(input("Enter the radius: "))
                print("T.S.A of Sphere: ", 4*3.14*a*a)

            elif ch==3:
                b = int(input("Enter the radius: "))
                print("T.S.A of Sphere: ", 4/3*3.14*a*a*a)

            else:
                print("Enter value invalid.")


    elif ch==10:
        while True:
            print("1. Lateral Surface HemiSphere")
            print("2. Total Surface HemiSphere")
            print("3. Volume of the HemiSphere")

            ch = int(input("Enter the value what you want to find: "))

            if ch==1:
                a = int(input("Enter the Radius: "))
                print("L.S.A of Sphere: ", 2*3.14*a*a)

            elif ch==2:
                a = int(input("Enter the Radius: "))
                print("T.S.A of Sphere: ", 3*3.14*a*a)

            elif ch==3:
                a = int(input("Enter the Radius: "))
                print("Volume of Sphere: ", 2/3*3.14*a*a*a)

    else:
        print("Enter value Invalid. ")





            






            

                

                

                





                                      


            




        
