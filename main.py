from PyQt5 import QtCore
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QLineEdit, QMainWindow,QLabel,QPushButton,QApplication,QGraphicsDropShadowEffect
from os import path
import sys


# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'UI_signup001.ui'))
from mainWindow import MainWindow


class LoginPage(QMainWindow, FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)  
        

        # Hide Widnow Frameless && Translucent Background
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Set Shadow around the Widget
        self.widget.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0))
        
        self.offset = None
        
        # Build Signals and Slots
        self.btn_close.clicked.connect(lambda : self.close())
        self.btn_min.clicked.connect(lambda : self.showMinimized())
        
        self.label_error.clear()
        self.btn_login.clicked.connect(self.login_check)
        
        ## Change Theme Signals
        self.btn_theme.setCheckable(True)
        
        self.btn_theme.clicked.connect(self.change_theme)
        
        self.default_theme()

        ## Show and Hide Password
        self.btn_show.setCheckable(True)
        
        self.btn_show.clicked.connect(self.show_pass)
        
        self.hide_pass()
        
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
        

    def change_theme(self):
        
        if self.btn_theme.isChecked():
            style = open("themes/login_page/dark.css","r")
            style = style.read()
            self.setStyleSheet(style)
            self.btn_theme.setText("G")
        else:
            self.default_theme()
    
    def default_theme(self):
        style = open("themes/login_page/light.css","r")
        style = style.read()
        self.setStyleSheet(style)
        self.btn_theme.setText("H")


    def show_pass(self):
        if self.btn_show.isChecked():
            self.lineEdit_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.hide_pass()

    def hide_pass(self):
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)


    def login_check(self):
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)
        if (self.lineEdit_user.text()).strip() == "HelloWorld" and (self.lineEdit_pass.text().strip()) == "A12345":
            main_page = MainWindow()
            self.close()
            main_page.show()
        else:
            self.label_error.setText("Username or Password Wrong!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    app.exec_()
