def control_rating(rating):
    if 65 <= rating <= 100:
        print('Academic performance within the norm.')
    else:
        print('Low academic performance!')


n = 3
for i in range(n):
    rating = int(input('Score: '))
    control_rating(rating)
