'''Question1: Create a Python class called "Rectangle" that represents a rectangle. The Rectangle class must have the following properties and methods:
##### Features:
- width (an integer)
- height (an integer)
##### Methods:
- area(self): A method that calculates and returns the area of ​​the rectangle.
- perimeter(self): A method that calculates and returns the perimeter of the rectangle.
- Create an instance of Rectangle class, set its width to 5 and height to 7, then print its area and perimeter.
'''

class Rectangle:
    
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return f"{self.width} cm genisliginde ve {self.height} cm yuksekligindeki bir dortgen"
        
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
               
rectangle1=Rectangle(5,7)

print(rectangle1)

# print(f"{rectangle1}'in alani {rectangle1.area} cm2 dir.")
# print(f"{rectangle1}'in cevresi {rectangle1.perimeter} cm dir.")

      
 