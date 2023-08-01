# import csv
# import random

# def read_csv_to_dict(filename):
#     with open(filename, mode='r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # This line is needed to skip the header
#         return {rows[1]: rows[0] for rows in csv_reader}

# def quiz(word_dict):
#     word, translation = random.choice(list(word_dict.items()))
#     user_answer = input(f'What is the German translation for the Romanian word "{word}"?\n')
#     print(f'You answered: {user_answer}')
#     print(f'The correct answer is: {translation}\n')

# def main():
#     filename = 'example.csv' 
#     word_dict = read_csv_to_dict(filename)
#     while True:
#         quiz(word_dict)

# if __name__ == "__main__":
#     main()

import csv
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

class TranslationQuiz(QWidget):
    def __init__(self, parent=None):
        super(TranslationQuiz, self).__init__(parent)
        self.setWindowTitle("German-Romanian Translation Quiz")
        self.word_dict = self.read_csv_to_dict('example.csv')  # Replace with your filename

        self.current_word, self.current_translation = self.pick_word()

        self.layout = QVBoxLayout()

        self.label = QLabel(f"What is the German translation for the Romanian word '{self.current_word}'?")
        self.layout.addWidget(self.label)

        self.entry = QLineEdit()
        self.layout.addWidget(self.entry)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.check_button)

        self.setLayout(self.layout)

    def read_csv_to_dict(self, filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # This line is needed to skip the header
            return {rows[1]: rows[0] for rows in csv_reader}

    def pick_word(self):
        return random.choice(list(self.word_dict.items()))

    def check_answer(self):
        user_answer = self.entry.text()
        if user_answer == self.current_translation:
            QMessageBox.information(self, "Result", "Correct!")
        else:
            QMessageBox.information(self, "Result", f"Incorrect. The correct answer is {self.current_translation}")
        self.current_word, self.current_translation = self.pick_word()
        self.label.setText(f"What is the German translation for the Romanian word '{self.current_word}'?")
        self.entry.clear()


def main():
    app = QApplication([])
    translator = TranslationQuiz()
    translator.show()
    app.exec_()

if __name__ == "__main__":
    main()
