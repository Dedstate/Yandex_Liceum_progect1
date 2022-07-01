import os
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import choice


with open("src/russian2.txt", encoding='utf-8') as f:
    ls = f.read().splitlines()
i = 0
while i < len(ls):
    print(i)
    if len(ls[i]) != 5:
        ls.pop(i)
    else:
        i += 1
# Сhange working directory
cur_dir = os.path.dirname(__file__)
os.chdir(cur_dir)


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("src/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.clicked)
        self.word = choice(ls)
        self.lineEdit.setText("_" * len(self.word))
        self.text = ""
        self.count = 0



    def attempt(self):
        if self.text not in self.word:
            self.count += 1
            self.lineEdit_2.setText("Вы ошиблись, осталсь попыток " + str(7 - self.count))
        else:
            for i in range(len(self.word)):
                if self.text[0] == self.word[i]:
                    t = self.lineEdit.text()
                    self.lineEdit.setText(t[:i] + self.text[0] + t[i + 1:])

        if "_" not in self.lineEdit.text():
            self.lineEdit_2.setText("Вы победили")

    def clicked(self):
        self.text = self.input.text()
        self.input.setText('')
        self.attempt()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


