import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class MyLineEdit(QLineEdit):
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)

    def focusInEvent(self, QFocusEvent):
        print('focus in event')
        # do custom stuff
        # super(MyLineEdit, self).focusInEvent(event)
        # self.emit(SIGNAL("Clicked()"))
        self.showkeyboard()

    def showkeyboard(self):
        # pass
        print('hello there inside onchanged')
        # os.system('osk')


class AddPatient(QWidget):
    def __init__(self):
        QWidget.__init__(self, parent=None)
        # super(AddPatient, self).__init__()
        # self.name = MyLineEdit(self)
        loadUi('UIs/PatientAdd.ui', self)
        self.conditions()
        self.registerbutton.clicked.connect(self.register)
        # self.name = MyLineEdit(self)
        # self.connect(self.lineEdit, SIGNAL("Clicked()"), self.showkeyboard())

    def resizeEvent(self, event):
        qr = self.frameGeometry()
        # print('height: '+str(qr.height()))
        # print('width: '+str(qr.width()))
        self.AddPat.move(qr.width()//2-210, qr.height()//2-200)

    def conditions(self):
        self.age.setValidator(QIntValidator())
        self.age.setMaxLength(3)
        self.phone.setValidator(QIntValidator())
        self.phone.setMaxLength(10)
        # self.phone.setInputMask('+99_9999999999')
        # name = QLineEdit(self)
        # name.textChanged[str].connect(self.onChanged)
        # name.event(mylineEdit().focusInEvent('Hello'))

    def register(self):
        name = self.name.text()
        age = self.age.text()
        gender = self.gender.currentText()
        phone = self.phone.text()

        print(name, age, gender, phone)


app = QApplication(sys.argv)
MainWindow = AddPatient()
widget = QtWidgets.QStackedWidget()
widget.addWidget(MainWindow)
widget.setWindowTitle('LarkAI')
widget.setMinimumHeight(600)
widget.setMinimumWidth(1024)
widget.show()
app.exec_()
