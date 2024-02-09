import math
from PIL import Image
import cowsay
from tabulate import tabulate
import sys



def main():
    instructions = [{"Key:": "1", "Calculate Area Moment of Inertia for:": "Rectangle"},
                    {"Key:": "2", "Calculate Area Moment of Inertia for:": "Triangle"},
                    {"Key:": "3", "Calculate Area Moment of Inertia for:": "Trapezoid"},
                    {"Key:": "4", "Calculate Area Moment of Inertia for:": "Circle"},
                    {"Key:": "5", "Calculate Area Moment of Inertia for:": "Ellipse"}]

    cowsay.tux("Welcome to Area MoI calculator!")

    if len(sys.argv)<2:
        print(tabulate(instructions, headers="keys", tablefmt="pretty"))
        Select = input("Selection No. : ")
    elif len(sys.argv)>2:
        print("Too many arguments")
    else:
        print(sys.argv[1])
        Select = sys.argv[1]


    cont = 'y'
    while cont == "y" or cont == "Y":
        #print(tabulate(instructions, headers="keys", tablefmt="pretty"))
        try:
            if Select == '':
                print(tabulate(instructions, headers="keys", tablefmt="pretty"))
                Select = input("Selection No. : ")
            match Select:
                case "1" |"Rectangle":
                    img = Image.open("Images/Rectangle.png")
                    img.show()

                    breadth = float(input("Please enter breadth (b) Rectangle : "))
                    height = float(input("Please enter height (h) Rectangle : "))
                    Rectangle(breadth, height)

                case "2" |"Triangle":
                    Triangle()

                case "3" |"Trapezoid":
                    img = Image.open("Images/Trapezoid.png")
                    img.show()

                    print("\nPlease enter following dimensions: ")
                    a = float(input("base 1 (a): "))
                    b = float(input("base 2 (b): "))
                    h = float(input("height (h): "))
                    Trapezoid(a,b,h)

                case "4" |"Circle":
                    Circle()

                case "5" | "Ellipse":
                    img = Image.open("Images/Ellipse.png")
                    img.show()

                    a = float(input("Please enter semi-major axis (a) Ellipse : "))
                    b = float(input("Please enter semi-minor axis (b) Ellipse : "))
                    Ellipse(a,b)

                case _:     #Default Case
                    try:
                        sys.argv[1] = ''
                    except IndexError:
                        print("\nInvalid ❌\n")
                    else:
                        print("\nInvalid ❌\n")
                        main()

        except ValueError:
            print("\nPlease enter numeric value!")
        else:               #else is only executed if the above try is executed successfully
            check = str(input("\nContinue? (y/n): "))
            if check == 'y' or check == 'n' or check == 'Y' or check == 'N':
                cont = check.lower()
                Select = ''

            else:
                while check != 'y' and check != 'n' and check != 'Y' and check != 'N':
                    print ("Invalid input")
                    check = str(input("\nContinue? (y/n): "))
                if check == 'y' or check == 'n' or check == 'Y' or check == 'N':
                    cont = check.lower()
                    Select = ''


    print("Thank you for visiting!")

def Circle ():

    class Circle_class():   # this is the class
        def __init__(self, type):    #to initialize the contents of a class #self takes the object
            if not type:
                raise ValueError("Missing Circle Type")
            self.type = type

        def dimensions(self):     #Method to prompt user for radius
            self.radius = float(input("\nPlease enter radius (r) of Circle : "))

        def calculate(self):  #Method to calculate the Area Moment of Inertia (MoI)
            match self.type:
                case 1:  #Full Circle MoI
                    img = Image.open("Images/Circle.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(1/4 * math.pi * self.radius**4, 3)
                    self.Iy = round(1/4 * math.pi * self.radius**4, 3)
                    self.A = math.pi * self.radius**2
                    self.name = "Circle"


                case 2: #Semicircle MoI
                    img = Image.open("Images/Semicircle.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(1/8 * math.pi * self.radius**4, 3)
                    self.Iy = round(1/8 * math.pi * self.radius**4, 3)
                    self.A = (math.pi * self.radius**2)/2
                    self.name = "Semicircle"

                case 3: #Quarter Circle MoI
                    img = Image.open("Images/Quarter Circle.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(1/16 * math.pi * self.radius**4, 3)
                    self.Iy = round(1/16 * math.pi * self.radius**4, 3)
                    self.A = (math.pi * self.radius**2)/4
                    self.name = "Quarter Circle"

                case 4: #Circular Ring MoI
                    img = Image.open("Images/Circular Ring.png")
                    img.show()

                    cir.dimensions()

                    thickness = float(input("Please enter thickness (t) of Circular Ring : "))
                    self.Ix = round(math.pi * self.radius**3*thickness, 3)
                    self.Iy = round(math.pi * self.radius**3*thickness, 3)
                    self.A = 2*math.pi*self.radius*thickness
                    self.name = "Circular Ring"

                case 5: #Quarter Circular Spandrel Ring MoI
                    img = Image.open("Images/Quarter Circular Spandrel.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(0.01825*self.radius**4, 3)
                    self.Iy = round(0.1370*self.radius**4, 3)
                    self.A = (1-(math.pi/4))*self.radius**2
                    self.name = "Quarter Circular Spandrel"

                case _:     #Default Case
                    print("\nInvalid ❌\n")
                    Circle()


        def __str__(self):    #always takes one argument that is self
            name = {"Shape" : self.name}
            momentOfInertia = {"Ix" : str(self.Ix)+" (Unit \u2074)", "Iy" : str(self.Iy)+" (Unit \u2074)"}  #unicode for superscript 4, to reflet the MoI unit
            Area = {"Area" : str(self.A)+" (Unit\u00b2)"}            #unicode for superscript 2     \u00b2
            geo_Properties = [name, momentOfInertia, Area]           #Geometrical Properties of Shape, to reflect Area unit

            return tabulate(geo_Properties, headers="keys", tablefmt="pretty")  #To return the MoI dictionary


            #List of Dictionaries for Selection Table
    instructions = [{"Key:": "1", "Circle Type:": "Full Circle"},
                    {"Key:": "2", "Circle Type:": "Semicircle"},
                    {"Key:": "3", "Circle Type:": "Quarter Circle"},
                    {"Key:": "4", "Circle Type:": "Circular Ring"},
                    {"Key:": "5", "Circle Type:": "Quarter Circular Spandrel Ring"}]

    print(tabulate(instructions, headers="keys", tablefmt="pretty"))     #Tabulate Library


    type = int(input("Selection No. : "))

    cir = Circle_class(type)
    cir.calculate()
    print(cir)


#Calculations Source:
# https://wp.optics.arizona.edu/optomech/wp-content/uploads/sites/53/2016/10/OPTI_222_W61.pdf
def Triangle ():

    class Triangle_class():   # this is the class
        def __init__(self, type):    #to initialize the contents of a class #self takes the object
            if not type:
                raise ValueError("Missing Triangle Type")
            self.type = type

        def dimensions(self):     #Method to prompt user for breadth and Height dimensions
            self.breadth = float(input("\nPlease enter breadth (b) of Triangle : "))
            self.height = float(input("Please enter height (h) of Triangle : "))

        def calculate(self):  #Method to calculate the Area Moment of Inertia (MoI)
            match self.type:
                case 1:  # Triangle MoI
                    img = Image.open("Images/Triangle.png")
                    img.show()

                    cir.dimensions()
                    c = float(input("Please enter offset (c) of Triangle : "))

                    self.Ix = round(1/36 * self.breadth * self.height**3,3)
                    self.Iy = round(1/36 * self.breadth * self.height*(self.breadth**2 - self.breadth * c + c**2), 3)
                    self.A = (self.breadth * self.height)/2
                    self.name = "Triangle"


                case 2: #Isosceles Triangle MoI
                    img = Image.open("Images/Isosceles Triangle.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(1/36 * self.breadth * self.height**3,3)
                    self.Iy = round(1/48 * self.breadth**3 * self.height,3)
                    self.A = (self.breadth * self.height)/2
                    self.name = "Isosceles Triangle"

                case 3: #Right Triangle MoI
                    img = Image.open("Images/Right Triangle.png")
                    img.show()

                    cir.dimensions()

                    self.Ix = round(1/36 * self.breadth * self.height**3,3)
                    self.Iy = round(1/36 * self.breadth**3 * self.height,3)
                    self.A = (self.breadth * self.height)/2
                    self.name = "Right Triangle"

                case _:     #Default Case
                    print("\nInvalid ❌\n")
                    Triangle()


        def __str__(self):    #always takes one argument that is self
            name = {"Shape" : self.name}
            momentOfInertia = {"Ix" : str(self.Ix)+" (Unit \u2074)", "Iy" : str(self.Iy)+" (Unit \u2074)"}  #unicode for superscript 4, to reflet the MoI unit
            Area = {"Area" : str(self.A)+" (Unit\u00b2)"}            #unicode for superscript 2     \u00b2
            geo_Properties = [name, momentOfInertia, Area]           #Geometrical Properties of Shape, to reflect Area unit

            return tabulate(geo_Properties, headers="keys", tablefmt="pretty")  #To return the MoI dictionary


            #List of Dictionaries for Selection Table
    instructions = [{"Key:": "1", "Triangle Type:": "Triangle"},
                    {"Key:": "2", "Triangle Type:": "Isosceles Triangle"},
                    {"Key:": "3", "Triangle Type:": "Right Triangle"},]


    print(tabulate(instructions, headers="keys", tablefmt="pretty"))     #Tabulate Library


    type = int(input("Selection No. : "))

    cir = Triangle_class(type)
    cir.calculate()
    print(cir)




def Rectangle (breadth, height):
    shape = 'Rectangle'

    Ix = round(1/12 * breadth * height**3, 3)
    Iy = round(1/12 * breadth**3 * height, 3)
    A = round(breadth * height)

    name = {"Shape" : shape}
    momentOfInertia = {"Ix" : str(Ix)+" (Unit \u2074)", "Iy" : str(Iy)+" (Unit \u2074)"}  #unicode for superscript 4, to reflet the MoI unit
    Area = {"Area" : str(A)+" (Unit\u00b2)"}            #unicode for superscript 2     \u00b2
    geo_Properties = [name, momentOfInertia, Area]           #Geometrical Properties of Shape, to reflect Area unit
    print(tabulate(geo_Properties, headers="keys", tablefmt="pretty"))  #To return the MoI dictionary

    return f'Ix = {Ix}, Iy = {Iy}'



# https://www.efunda.com/math/areas/IsosTrapezoid.cfm
def Trapezoid (a,b,h):
    shape = 'Trapezoid'

    Ix = round(1/12 * h**3 * (3*a+b), 3)
    Iy = round(1/48 * h* (a+b) * (a**2 + 7*b**2), 3)
    A = (h*(a+b))/2


    name = {"Shape" : shape}
    momentOfInertia = {"Ix" : str(Ix)+" (Unit \u2074)", "Iy" : str(Iy)+" (Unit \u2074)"}  #unicode for superscript 4, to reflet the MoI unit
    Area = {"Area" : str(A)+" (Unit\u00b2)"}            #unicode for superscript 2     \u00b2
    geo_Properties = [name, momentOfInertia, Area]           #Geometrical Properties of Shape, to reflect Area unit

    print(tabulate(geo_Properties, headers="keys", tablefmt="pretty"))  #To return the MoI dictionary

    return f'Ix = {Ix}, Iy = {Iy}'



def Ellipse (a,b):
    shape = 'Ellipse'

    Ix = round(1/4* math.pi * a * b**3,3)
    Iy = round(1/4* math.pi * a**3 * b,3)
    A = round(math.pi * a * b)

    name = {"Shape" : shape}
    momentOfInertia = {"Ix" : str(Ix)+" (Unit \u2074)", "Iy" : str(Iy)+" (Unit \u2074)"}  #unicode for superscript 4, to reflet the MoI unit
    Area = {"Area" : str(A)+" (Unit\u00b2)"}                 #unicode for superscript 2     \u00b2
    geo_Properties = [name, momentOfInertia, Area]           #Geometrical Properties of Shape, to reflect Area unit

    print(tabulate(geo_Properties, headers="keys", tablefmt="pretty"))  #To return the MoI dictionary
    return f'Ix = {Ix}, Iy = {Iy}'

if __name__ == "__main__":
    main()
