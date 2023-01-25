import sys
import json
import random
import datetime
import time
from words_per_second_ui import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import pyqtSlot, QThreadPool

with open("paragraphs.json", encoding="utf-8") as paragraph_json:
    paragraph_dict = json.load(paragraph_json)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread_manager = QThreadPool()
        self.ui.typed_text.textChanged.connect(self.compare_text)
        self.start_time = datetime.datetime.now()
        self.timer_run = False
        self.ui.text_results.setText("Your score is: ")
        self.ui.start_button.clicked.connect(self.start_timer_safely)
        self.ui.typed_text.setEnabled(False)
        self.ui.stop_button.clicked.connect(self.stop_timer)
        self.show()

    def create_word_list_to_type(self):
        word_list = self.ui.text_to_type.text().split(" ")
        return word_list

    def create_word_list_typed(self):
        word_list = self.ui.typed_text.toPlainText().split(" ")
        return word_list

    def compare_text(self):
        to_type = self.create_word_list_to_type()
        typed = self.create_word_list_typed()
        for word_index in range(len(typed)):
            word = typed[word_index]
            for char_index in range(len(word)):
                try:
                    if not word[char_index] == to_type[word_index][char_index]:
                        cursor = self.ui.typed_text.textCursor()
                        cursor.deletePreviousChar()
                        cursor.MoveOperation("End")
                    else:
                        pass
                except IndexError:
                    cursor = self.ui.typed_text.textCursor()
                    cursor.deletePreviousChar()
                    cursor.MoveOperation("End")

    def start_timer(self):
        start_time = datetime.datetime.now()
        while self.timer_run:
            new_time = 60 - int((datetime.datetime.now() - start_time).total_seconds())
            self.ui.timer.display(new_time)
            if new_time == 0:
                self.timer_run = False

        self.ui.timer.display(60)
        self.set_score()
        self.ui.typed_text.setEnabled(False)
        self.ui.start_button.setEnabled(True)

    def start_timer_safely(self):
        self.pick_paragraph()
        self.ui.typed_text.setEnabled(True)
        self.ui.typed_text.setFocus()
        self.timer_run = True
        self.ui.start_button.setEnabled(False)
        self.thread_manager.start(self.start_timer)

    def set_score(self):
        score = len(self.ui.typed_text.toPlainText().split(" "))
        self.ui.text_results.setText(f"Your score is: {score}")

    def pick_paragraph(self):
        paragraph = paragraph_dict[str(random.randint(1, len(paragraph_dict)))]
        self.ui.text_to_type.setText(paragraph)

    def stop_timer(self):
        self.timer_run = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()

    sys.exit(app.exec())
