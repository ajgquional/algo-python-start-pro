class Land():
   def __init__(self, length, width):
       self.length = length
       self.width = width
   def print_info(self):
       print(f'Plot length: {self.length}, width: {self.width}.')
   def calc_perimeter(self):
       self.perimeter = (self.length + self.width) * 2
       return self.perimeter
   def calc_area(self):
       self.area = self.length * self.width
       return self.area
 
a = int(input('Enter length: '))
b = int(input('Enter width: '))
land_plot = Land(a, b)
land_plot.print_info()
print('Plot perimeter:', land_plot.calc_perimeter())
print('Plot area:', land_plot.calc_area())
