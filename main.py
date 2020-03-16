import sys
from untitled import Ui_MainWindow
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt


class Guess_the_number(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)   # 继承主窗口类
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = Guess_the_number()

    MainWindow.show()
    sys.exit(app.exec_())
