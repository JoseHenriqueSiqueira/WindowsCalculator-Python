from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sys

class Window(QWidget):
    signal=pyqtSignal(str)
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(320, 470)
        loadUi(r"Ui/Interface.ui",self)
        self.op=None
        self.nm1=None
        self.nm2=None
        self.temp=0
        self.negative=""
        self.fontreturn=None
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("^-?\d+$[0-9]*"),self.lineEdit))
        self.signal.connect(self.sinal)
        self.btn1.clicked.connect(lambda: self.number('1'))
        self.btn2.clicked.connect(lambda: self.number('2'))
        self.btn3.clicked.connect(lambda: self.number('3'))
        self.btn4.clicked.connect(lambda: self.number('4'))
        self.btn5.clicked.connect(lambda: self.number('5'))
        self.btn6.clicked.connect(lambda: self.number('6'))
        self.btn7.clicked.connect(lambda: self.number('7'))
        self.btn8.clicked.connect(lambda: self.number('8'))
        self.btn9.clicked.connect(lambda: self.number('9'))
        self.btn0.clicked.connect(lambda: self.number('0'))
        self.btndel.clicked.connect(lambda: self.signal.emit("del"))
        self.btnreset.clicked.connect(lambda: self.signal.emit("reset"))
        self.btnsum.clicked.connect(self.bttsum)
        self.btnsub.clicked.connect(self.bttsub)
        self.btnmult.clicked.connect(self.bttmult)
        self.btnresult.clicked.connect(self.result)

    def number(self,number):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText(number)
                self.temp=1
            else:
                self.lineEdit.setText(text+number)
            self.nm2=self.lineEdit.text()
            self.signal.emit('fontsize')
            return
        else:
            if self.temp==0:
                self.lineEdit.setText(number)
                self.temp=1
            else:
                self.lineEdit.setText(text+number)
            self.nm1=self.lineEdit.text()
            self.signal.emit('fontsize')
            return

    def bttsum(self,event):
        operation={'-':'+-','+':'+1','x':'+x'}
        self.signal.emit('fontsize')
        if self.op and self.nm2 and self.nm1:
            return self.signal.emit(operation.get(self.op))
        elif self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op="+"
            self.temp=0
            self.label.setText(self.nm1+" +")
        elif self.nm1:
            self.op="+"
            self.temp=0
            self.label.setText(self.nm1+" +")

    def bttsub(self,event):
        operation={'+':'-+','-':'-1','x':'-x'}
        self.signal.emit('fontsize')
        if self.op and self.nm2 and self.nm1:
            return self.signal.emit(operation.get(self.op))
        elif self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op="-"
            self.temp=0
            self.label.setText(self.nm1+" -")
        elif self.nm1:
            self.op="-"
            self.temp=0
            self.label.setText(self.nm1+" -")
        elif self.lineEdit.text()=="0":
            self.negative="s"
            self.label.setText("0 -")
       
    def bttmult(self,event):
        self.signal.emit('fontsize')
        operation={'+':'x+','-':'x-','x':'x1'}
        if self.op and self.nm2 and self.nm1:
            self.signal.emit(operation.get(self.op))
        elif self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op="x"
            self.temp=0
            self.label.setText(self.nm1+" x")
        elif self.nm1:
            self.op="x"
            self.temp=0
            self.label.setText(self.nm1+" x")

    def result(self,event):
        self.signal.emit(self.op)
        self.signal.emit('fontsize')

    def keyPressEvent(self, event):
        numbers_key = (Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9)
        operations_key = {Qt.Key_Minus: "-", Qt.Key_Plus:"+", Qt.Key_Asterisk:"x", Qt.Key_Slash:"/", Qt.Key_Equal:"=", Qt.Key_Enter:"=", Qt.Key_Return:"="}
        operations={"-":lambda: self.btnsub.click(), "+": lambda: self.btnsum.click(), "x": lambda: self.btnmult.click(), "/": lambda: print("/"), "=": lambda: self.btnresult.click()}
        if event.key() in numbers_key:
            n = event.key() - Qt.Key_0 # convert the key code to the corresponding number
            self.number(str(n))
        elif event.key() in operations_key:
            operations.get(operations_key.get(event.key()))()

    def sinal(self,response):
        print(response)
        def sub_complement():
            if int(self.nm2) > int(self.nm1) and int(self.nm1) > 0:
                return (int(self.nm2) - int(self.nm1)) * -1
            elif int(self.nm2) > 0 and int(self.nm1) < 0 and self.op == "+":
                return int(self.nm2) + int(self.nm1)
            else:
                return int(self.nm1) - int(self.nm2)
        operations = {
            "+": lambda: int(self.nm1) + int(self.nm2),
            "-": lambda: int(self.nm1) - int(self.nm2),
            "x": lambda: int(self.nm1) * int(self.nm2),
        }
        complements={
            "+1": operations.get('+'),
            "-+": operations.get('+'),
            "x+": operations.get('+'),
            "-1": operations.get('-'),
            "+-": sub_complement,
            "x-": sub_complement,
            "x1": operations.get('x'),
            "-x": operations.get('x'),
            "+x": operations.get('x')
        }
        if response in operations:
            try:
                result = operations[response]()
                self.lineEdit.setText(str(result))
                self.label.setText(f"{self.nm1} {response} {self.nm2} =")
                self.nm1 = str(result)
                self.nm2 = None
                self.temp = 0
                self.op = ""
            except ZeroDivisionError:
                self.lineEdit.setText("Não é possível dividir por zero")
        elif response in complements:
            try:
                result = complements[response]()
                self.lineEdit.setText(str(result))
                self.label.setText(f"{str(result)} {response[0]}")
                self.nm1 = str(result)
                self.nm2 = None
                self.temp = 0
                self.op = response[0]
            except ZeroDivisionError:
                self.lineEdit.setText("Não é possível dividir por zero")
        elif response=="reset":
            self.op=""
            self.nm1=None
            self.nm2=None
            self.temp=0
            self.label.setText('')
            self.lineEdit.setText('0')
            self.signal.emit('fontsize')
        elif response=="del":
            if len(self.lineEdit.text()) == 1:
                self.lineEdit.setText("0")
                self.temp=0
            else:
                self.fontreturn=True
                Str = self.lineEdit.text()[:len(self.lineEdit.text())-1]
                self.lineEdit.setText(Str)
                self.signal.emit('fontsize')
        elif response=="fontsize":
                font=self.lineEdit.font()
                font_metrics = QFontMetrics(font)
                text = self.lineEdit.text()
                text_width = font_metrics.width(text)
                widget_widt=self.lineEdit.width()
                font_size=font.pointSize()
                if text_width>widget_widt:       
                    while text_width > widget_widt:
                        font_size -= 1
                        font.setPointSize(font_size)
                        font_metrics = QFontMetrics(font)
                        text_width = font_metrics.width(text)
                    self.lineEdit.setFont(font)
                    return
                while self.fontreturn and len(self.lineEdit.text())>=10 and font.pointSize()<35:
                    font.setPointSize(font.pointSize() + 1)
                    self.lineEdit.setFont(font)
                    self.fontreturn=None
                if len(self.lineEdit.text())<12 and font.pointSize()<35:
                    font.setPointSize(35)
                    self.lineEdit.setFont(font)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
