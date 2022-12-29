import sys
import keyboard  # using module keyboard

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 32),
                QtWidgets.qApp.desktop().availableGeometry()
        ))
        self.layout = QVBoxLayout()
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.read_hotkey():  # if key 'q' is pressed 
                
                    self.label = QLabel("Key was pressed")
                    break  # finishing the loop
            except:
                break
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
    
    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()

