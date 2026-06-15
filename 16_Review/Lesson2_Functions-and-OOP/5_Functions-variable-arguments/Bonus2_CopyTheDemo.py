from count_services import count_services

service = input('For which of the services would you like to order services (1 - Instagram, 2 - YouTube)? ')
if service == '1':
    plan = int(input('Enter the number of accounts to create a content plan for: '))
    stories = int(input('Enter the number of stories: '))
    posts = int(input('Enter the number of posts: '))
    total, categories = count_services(plan = plan, stories = stories, posts = posts)
else:
    cover = int(input('Enter the number of videos that need thumbnails: '))
    editing = int(input('Enter the number of videos that need editing: '))
    total, categories = count_services(cover = cover, editing = editing)


print(f'Services: {total}, categories: {categories}.')
print('Our specialists have already started working on it!')
