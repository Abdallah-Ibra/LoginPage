from PyQt5 import QtCore
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QLineEdit, QMainWindow,QLabel,QPushButton,QApplication
from os import path
import sys


# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'UI_Window.ui'))


class MainWindow(QMainWindow,FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # Frameless Window and Translucent Background
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.offset = None
    
    
        # Configure Signals and Slots
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_min.clicked.connect(lambda: self.showMinimized())
        
        ## Change Theme Signals
        self.btn_theme.setCheckable(True)
        
        self.btn_theme.clicked.connect(self.change_theme)
        
        self.default_theme()

        self.update()

        
    
    # Make frameless dragable
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def default_theme(self):
        style = open("themes/main_window/light.css")
        style = style.read()
        self.setStyleSheet(style)
        self.btn_theme.setText("H")


    def change_theme(self):
        if self.btn_theme.isChecked():
            style = open("themes/main_window/dark.css")
            style = style.read()
            self.setStyleSheet(style)
            self.btn_theme.setText("G")
        else:
            self.default_theme()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()    
    app.exec_()