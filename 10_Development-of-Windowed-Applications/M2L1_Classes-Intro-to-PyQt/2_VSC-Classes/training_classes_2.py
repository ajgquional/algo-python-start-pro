class Title():
    # constructor
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True

    # methods
    def hide(self):
        self.appearance = False
        print(self.title, '- hidden')
    
    def show(self):
        self.appearance = False
        print(self.title, '- displayed')
    
    def print_info(self):
        print('Button:', self.title)
        print('Position:', '(' + str(self.x) + ',' + str(self.y) + ')')
        print('Visibility:', self.appearance)

# create 2 labels
main_title = Title('Find out the winner now!', 150, 50)
main_title.print_info()

# border
print("="*50 + '\n')

rules_title = Title('There can only be one winner', 150, -100)
rules_title.print_info()

# border
print("="*50 + '\n')

# hide the 2nd label
rules_title.hide()
