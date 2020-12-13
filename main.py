# !usr/bin/python3.9
# _*_ coding: utf_8 _*_

import sys
import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_MainWindow


class Application(QWidget):


    def __init__(self):
        super().__init__()
        self.init_UI()
    

    def init_UI(self):
        self.ui = uic.loadUi("./desing.ui")
        self.ui.show()




if __name__ == "__main__":
   app = QApplication(sys.argv)
   example_app = Application()
   app.exec_()