class Student():
    def __init__(self, name, average_grade):
        self.name = name
        self.average_grade = average_grade  
        self.course = '-'

    def print_info(self):
        print('Student: ', self.name)
        print('Average grade: ', self.average_grade)
        print('Attending elective course: ', self.course)

    def select_course(self):
        course = input('Enter the course name: ')
        self.course = course
 

student = Student('Darius Steph', '4.8')
student.print_info()
student.select_course()
student.print_info()
