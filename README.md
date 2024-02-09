# AMoI Calculator
    #### Video Demo:  <[https://www.youtube.com/watch?v=focpEf84uQ0&t=17s](https://youtu.be/ykPuTYBtmQw?si=NF8jj9VqJKQASzWq)>
    #### Description: Area Moment of Inertia Calculator
![image alt test](https://efficientengineer.com/wp-content/uploads/second_moment_of_area.jpg)

AMoI is a python-based calculator that computes the Area Moment of Inertia for basic shapes, including:

- Rectangle ▭
- Triangle △
- Trapezoid ⏢
- Circle ◯
- Ellipse ⬭

## Features

- Compute the Area of shapes
- Compute the Area Moment of Inertia for shapes

## What is Area Moment of Inertia (Explanation)?

The Area Moment of Inertia, also known as the Second Moment of Inertia, is a measurement that indicates a shape's resistance to bending by considering its area distribution around the axis of bending. Engineers utilize this measurement in designing structures like beams, mechanical components, etc., to ensure they can endure specific bending forces at particular locations without failing. By comparing the Area Moments of Inertia along both axes (Ix and Iy), engineers can determine the optimal position corresponding to the maximum allowable Moment of Inertia. Consequently, this Moment of Inertia (Ix or Iy) will be the most robust in resisting the bending force acting along its axis direction.
![image alt test](https://thestructuralblog.com/wp-content/uploads/001-300x199.jpg)
As depicted in the figure above, it is evident that beam 1 exhibits greater resistance to bending due to its higher Area Moment of Inertia along the Vertical axis (Ix).

#### Unit
The unit of Area Moment of Inertia is length raised to the power of 4, represented as (Length Unit)^4^.

#### Formulas
The second moment of area for the x-axis (Ix), is given as:
Ix = ∫y^2^dA

The second moment of area for the y-axis (Iy), is given as:
Iy = ∫x^2^dA

The moments of inertia for several common area shapes have been calculated about their centroidal axes using the equations mentioned above, and they are listed in Mechanics of Materials books referenced below.

Alternatively, click on the following link to view the equations for each shape.
```
https://wp.optics.arizona.edu/optomech/wp-content/uploads/sites/53/2016/10/OPTI_222_W61.pdf
```
## Python Code

#### Libraries imported:

- [x] sys
- [x] math
- [x] cowsay
- [x] PIL
- [x] tabulate
-

#### Coding concepts used:

- [x] OOP
Object-oriented programming was employed to create a class for the Circle shape since all shapes share some common attributes like radius.
Similarly, a class was created for the Triangle shape, given attributes such as Triangle's breadth and height.
Both of these classes incorporated methods such as _ _ init _ _,  _ _str _ _, along with user-defined methods for computing the Area Moment of Inertia
-[X] sys
Allows users to select the shape for which they wish to compute its Area Moment of Inertia from options such as ["Rectangle", "Triangle", "Trapezoid", "Circle", "Ellipse"]. In case, the user does not enter a shape, a selection table will be prompt them to choose the desired shape when the program is executed.
-[X] Match-Case
Case-Match was utilized to match the desired shape inputed by the user in order to calculate the area moment of inertia and execute out the specific shape function.
-[X] if Conditions
-[X] while
To prompt the user to continue the program or end it.
-[X] list
-[X] dictionary
A list of dictionaries was used to display the selection tables using the Tabulate library.
-[X] try and except
Try and except are used to handle errors when the user enters an invalid value type.

## Reference
- Beer, F. P., Johnston, E. R., DeWolf, J. T., Mazurek, D. F., & Sanghi, S. (2020). Mechanics of Materials 8th Edition, SI Units.
- CS50’s Introduction to Programming with Python. (n.d.). https://cs50.harvard.edu/python/2022/
- Hibbeler, R. C. (2017). Mechanics of materials in SI units.

