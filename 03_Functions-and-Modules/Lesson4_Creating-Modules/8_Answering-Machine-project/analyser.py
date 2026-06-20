def analyse(phrase):
    phrase = phrase.lower()
    res = phrase.find('sch')
    if res != -1:
        print_schedule()

    res = phrase.find('coach')
    if res != -1:
        print_trainer_info()

    res1 = phrase.find('pay')
    res2 = phrase.find('mon')
    if res1 != -1 or res2 != -1:
        calc_money()


def print_schedule():
    print('training schedule:')
    print('MO 15:00 - general strength training\nWE 15:00 - swimming pool\nFR 17:00 - swimming pool')


def print_trainer_info():
    print('Head coach: John Smith, +44 113 666 5566')
    print('Swimming trainer: Will Green, +44 113 666 5566')


def calc_money():
    trainings = int(input('How many training sessions have you attended?'))
    print('Amount due:', trainings*1500)
