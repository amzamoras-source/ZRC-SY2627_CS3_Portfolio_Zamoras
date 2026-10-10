# Watch the video, then recreate the Rectangle class code demonstrated in the video, with
# width and height as private members. Pay close attention to how the @property decorator is
# used, how getter and setter methods are named, and how these methods work like regular
# variables.
# Ensure that your code runs without any errors.
# Then, answer this reflection question in your notebook.
# ➢ How does using @property make your code easier to read compared to using
# traditional get_ and set_ methods?

class Rectangle: 
    def __init__(self, width, height):
        self._width = width  #protected attribute
        self._height = height  #protected attribute

    @property
    def width(self):
        return f"{self._width:.1f}.cm"

    @property
    def height(self):
        return f"{self._height:.1f}.cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero!")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")


rectangle = Rectangle(3, 4)

print(rectangle.width)  # Output: 3.0.cm
print(rectangle.height)  # Output: 4.0.cm

rectangle.width = 0
rectangle.height = 0

del rectangle.width
del rectangle.height 

