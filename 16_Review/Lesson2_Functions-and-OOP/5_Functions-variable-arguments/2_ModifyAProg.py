def print_info(**kwargs):
   for key in kwargs:
       print('Service –', key, ', price –', kwargs[key])
print_info(stories = 100, management = 1000)
