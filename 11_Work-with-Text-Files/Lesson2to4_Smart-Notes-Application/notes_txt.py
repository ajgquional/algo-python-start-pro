from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
from pathlib import Path

app = QApplication([])
notes = []
script_dir = Path(__file__).resolve().parent

# app interface:
# app window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)

# app window widgets
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')

button_note_create = QPushButton('Create note') # window with field "Enter note name" appears
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')

field_text = QTextEdit()

# arrangement of widgets by layouts
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

# app functionality:
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])


def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name: ")
    if ok and note_name != "":
        note = [note_name, '']
        notes.append(note)
        list_notes.addItem(note[0])
        print(notes)
        note_file = script_dir / (str(len(notes)-1) + ".txt")
        with open(note_file, "w", encoding='utf-8') as file:
            file.write(note[0]+'\n')
            file.write(note[1]+'\n')


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                note_file = script_dir / (str(notes.index(note)) + ".txt")
                with open(note_file, "w", encoding='utf-8') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                break
        print(notes)
    else:
        print("Note to save is not selected!")


def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for index, note in enumerate(notes):
            if note[0] == key:
                notes.pop(index)
                break
        list_notes.clear()
        field_text.clear()
        list_notes.addItems([note[0] for note in notes])

        for index, note in enumerate(notes):
            note_file = script_dir / (str(index) + ".txt")
            with open(note_file, "w", encoding='utf-8') as file:
                file.write(note[0] + '\n')
                file.write(note[1] + '\n')

        stale_index = len(notes)
        stale_file = script_dir / (str(stale_index) + ".txt")
        while stale_file.exists():
            stale_file.unlink()
            stale_index += 1
            stale_file = script_dir / (str(stale_index) + ".txt")
        print(notes)
    else:
        print("Note to delete is not selected!")


# event handling
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)

# app startup 
notes_win.show()

name = 0
note = []
while True:
    filename = str(name)+".txt"
    note_file = script_dir / filename
    try:
        with open(note_file, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        while len(note) < 2:
            note.append('')
        
        note = note[:2]
        notes.append(note)
        note = []
        name += 1

    except IOError:
        break

print(notes)
for note in notes:
    list_notes.addItem(note[0])

app.exec_()
