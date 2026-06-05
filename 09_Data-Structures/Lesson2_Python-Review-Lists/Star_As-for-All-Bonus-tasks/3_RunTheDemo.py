def get_info():
    student_name = input('Student’s last name: ')
    student_subjects = input('Core subjects: ')
    student_subjects = student_subjects.replace(',', '')
    student_subjects = student_subjects.split(' ')
    student_subjects.sort()
    student = list()
    student.append(student_name)
    student.append(student_subjects)
    return student


def print_info(student):
    print('Student profile')
    print('Last name -', student[0])
    print('Core subjects:')
    i = 1

    for subject in student[1]:
        print(i, '-', subject)
        i += 1


student1 = get_info()
student2 = get_info()
print_info(student1)
print_info(student2)
