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
        self.event_hundler()
    

    def init_UI(self):
        self.ui = uic.loadUi("./desing.ui")
        self.ui.show()
    

    def event_hundler(self):
        
        self.event_btn()
    
    
    def event_btn(self):
        self.ui.BtnSendMessage.clicked.connect(self.send_message)
    

    def send_message(self, event):
        text_message = self.ui.TextInputMessage.toPlainText().rstrip()
        if text_message != '':
            self.ui.TextInputMessage.clear()
            self.ui.Messages.append(text_message)
        




if __name__ == "__main__":
   app = QApplication(sys.argv)
   example_app = Application()
   app.exec_()