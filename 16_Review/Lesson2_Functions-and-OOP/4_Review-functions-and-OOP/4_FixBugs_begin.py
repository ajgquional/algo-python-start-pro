class My_success():
    def __init__(self,value):
        self.value_of_success = value
    def check_success():
        if value_of_success > 4.0:
            return 'Startup was successful'
        elif value_of_success < 4.0 and value_of_success >= 3.0:
            return 'Startup went well'
        return 'The project needs some work'
rate = float(input('App rating'))
object = My_success(rate)
print(object.check_success())