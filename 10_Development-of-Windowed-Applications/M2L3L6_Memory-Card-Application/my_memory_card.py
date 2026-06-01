from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
    QPushButton, QLabel)
from random import randint, shuffle 


class Question():
    '''contains a question, a correct answer and three incorrect ones'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(
        Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(
        Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(
        Question('Yakut national house', 'Urasa', 'Yurta', 'Igloo', 'Khata'))


app = QApplication([])

btn_OK = QPushButton('Reply') # reply button
lb_Question = QLabel('The most difficult question in the world!') # question text

RadioGroupBox = QGroupBox("Answer options")  # on-screen group of radio buttons
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup() # to group radio buttons to control their behavior
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # vertical guides inside the horizontal one
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answer options in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answer options in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  # columns placed in one line

RadioGroupBox.setLayout(layout_ans1) # the "panel" with answer options is ready 

AnsGroupBox = QGroupBox("Test results")
lb_Result = QLabel('are you right or not?') # here it will be written if you are "right" or "wrong"
lb_Correct = QLabel('answer will be here!') # here will be the text of the correct answer

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

EndGroupBox = QGroupBox('Game over')
lb_End = QLabel()
lb_End.setAlignment(Qt.AlignCenter)
layout_end = QVBoxLayout()
layout_end.addWidget(lb_End)
EndGroupBox.setLayout(layout_end)
EndGroupBox.hide()

layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result 
layout_line3 = QHBoxLayout() # "Answer" button

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(EndGroupBox)
AnsGroupBox.hide() # hide the answer panel, the question panel should be visible first 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content elements


def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    EndGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next')


def show_question():
    ''' show question panel '''
    lb_Question.show()
    EndGroupBox.hide()
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Reply')
    RadioGroup.setExclusive(False) # removed the restrictions so as to reset the radio button choice
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # returned the restrictions, now only one radio button can be selected


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' function writes the values of the question and answers to the corresponding widgets, 
    at the same time the answer options are distributed randomly'''
    shuffle(answers) # shuffled the list of buttons, now some random button is first in the list
    answers[0].setText(q.right_answer) # fill the first element of the list with the right answer, the rest with wrong ones
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # question
    lb_Correct.setText(q.right_answer) # reply
    show_question() # show question panel 


def show_correct(res):
    ''' show the result - set the text passed to the "result" inscription and show the panel we need '''
    lb_Result.setText(res)
    show_result()


def print_statistics():
    ''' print quiz statistics and the current rating to the console '''
    rating = 0
    if window.total:
        rating = (window.score / window.total) * 100
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
    print('Rating: ', rating, '%')


def show_end_game():
    ''' show the final game state in the main window '''
    rating = 0
    if window.total:
        rating = (window.score / window.total) * 100
    lb_Question.hide()
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    EndGroupBox.show()
    lb_End.setText(
        'The game is over!\n\n'
        f'Total questions: {window.total}\n'
        f'Right answers: {window.score}\n'
        f'Rating: {rating:.2f}%'
    )
    btn_OK.setEnabled(False)


def check_answer():
    ''' if any answer option is chosen, we need to check and show the answer panel'''
    if answers[0].isChecked():
        # right answer!
        show_correct('Right!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # wrong answer!
            show_correct('Wrong answer!')
    print_statistics()
    

def next_question():
    ''' asks a random question from the list '''
    if not window.remaining_questions:
        show_end_game()
        return
    cur_question = randint(0, len(window.remaining_questions) - 1)
    q = window.remaining_questions.pop(cur_question) # picked a question
    ask(q) # asks


def click_OK():
    ''' determines whether to show another question or check the answer to this one '''
    if btn_OK.text() == 'Reply':
        check_answer() # answer check
    else:
        next_question() # next question


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK) # by clicking on the button, we choose what exactly happens

window.score = 0
window.total = len(questions_list)
window.remaining_questions = questions_list.copy()
next_question()
window.resize(400, 300)
window.show()
app.exec()