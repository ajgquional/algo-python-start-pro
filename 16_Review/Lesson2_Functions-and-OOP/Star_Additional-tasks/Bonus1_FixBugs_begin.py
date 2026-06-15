class Land():
   def _init__(self, length, width):
       self.length = length
       self.width = width
   def print_info():
       print(f'plot length: {length}, width: {width}.')
   def calc_perimeter():
       self.perimeter = (length + width) * 2
       return self.perimeter
   def calc_area():
       self.area = length * width
       return self.area
 
a = int(input('Enter length:'))
b = int(input('Enter width:'))
land_plot = Land(a, b)
land_plot.print_info()
print('Plot perimeter:', calc_perimeter())
print('Plot area:', calc_area())