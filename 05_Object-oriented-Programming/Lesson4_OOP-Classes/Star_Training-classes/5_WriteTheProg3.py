class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print('Given a rectangle with length of', self.length, 'and width of', self.width)

    def calc_perimeter(self):
        self.perimeter = (self.length + self.width) * 2
        return self.perimeter
    
    def calc_area(self):
        self.area = self.length * self.width
        return self.area
 

a = int(input('Enter length: '))
b = int(input('Enter width: '))
rect = Rectangle(a, b)
rect.print_info()
print('Its perimeter:', rect.calc_perimeter())
print('Its area:', rect.calc_area())
