def print_info(data):
    for key in data:
        print('Service –',key,', price –',data[key])
prices = {'stories':100,'management':1000}
print_info(prices)
