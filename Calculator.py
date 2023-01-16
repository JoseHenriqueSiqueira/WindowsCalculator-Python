from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(320, 470)
        loadUi(r"Ui/Interface.ui",self)
        self.operations = {
            "+": lambda: float(self.nm1) + float(self.nm2),
            "-": lambda: abs(float(self.nm1)) - abs(float(self.nm2)) if self.nm2!='0' else (abs(float(self.nm1)) - abs(float(self.nm2)))*-1,
            "x": lambda: float(self.nm1) * float(self.nm2),
            "÷": lambda: float(self.nm1) / float(self.nm2),
        }
        self.op=None
        self.nm1=None
        self.nm2=None
        self.temp=0
        self.negative=""
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("^-?\d+$[0-9]*"),self.lineEdit))
        self.lineEdit.textChanged.connect(self.updatefont)
        for i in range(10):
            button = getattr(self, f"btn{i}")
            button.clicked.connect(self.number)
        self.btndel.clicked.connect(self.delete)
        self.btnreset.clicked.connect(self.reset)
        self.btnsum.clicked.connect(lambda: self.operation("+"))
        self.btnsub.clicked.connect(lambda: self.operation("-"))
        self.btnmult.clicked.connect(lambda: self.operation("x"))
        self.btndiv.clicked.connect(lambda: self.operation("÷"))
        self.btnresult.clicked.connect(self.result)
        self.btndecimal.setText(QLocale().decimalPoint())
        self.btndecimal.clicked.connect(self.number)

    def number(self):
        number = self.sender().text()
        text=self.lineEdit.text()
        decimal=QLocale().decimalPoint()
        if number == decimal and text.count(decimal) > 0:
            return
        if self.op:
            if self.temp==0 and number!=decimal:
                self.lineEdit.setText(number)
            else:
                self.lineEdit.setText(text+number)
            self.temp=1
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0 and number!=decimal:
                self.lineEdit.setText(number)
            else:
                self.lineEdit.setText(text+number)
            self.temp=1
            self.nm1=self.lineEdit.text()
            return

    def operation(self, op):
        if self.op and self.nm2 and self.nm1:
            try:
                self.nm1 = QLocale().toFloat(self.nm1)[0]
                self.nm2 = QLocale().toFloat(self.nm2)[0]
                result=self.operations.get(self.op)()
                formatted_result=QLocale().toString(result, 'f', 2)
                if ',' in formatted_result:
                    parts = formatted_result.split(',')
                    if parts[1] and all(c == '0' for c in parts[1]):
                        formatted_result = parts[0] # remove trailing zeros   
                self.nm1=formatted_result
                self.nm2=None
                self.lineEdit.setText(self.nm1)
                self.temp=0
                self.label.setText(self.nm1+" "+ op)
                self.op=op
            except ZeroDivisionError:
                self.lineEdit.setText("Zero Division")
        elif self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op=op
            self.temp=0
            self.label.setText(self.nm1+" "+ op)
        elif self.nm1:
            self.op=op
            self.temp=0
            self.label.setText(self.nm1+" "+ op)
        elif self.lineEdit.text()=="0" and op=='-':
            self.negative="s"
            self.label.setText("0 -")
        elif self.lineEdit.text()=="0" and op!='-':
            self.negative=""
            self.label.setText("0 "+op)
            self.nm1='0'
            self.op=op
            self.temp=0

    def result(self):
        if self.op in self.operations and self.nm2:
            try:
                textn1=self.nm1
                textn2=self.nm2
                self.nm1 = QLocale().toFloat(self.nm1)[0]
                self.nm2 = QLocale().toFloat(self.nm2)[0]
                result=self.operations.get(self.op)()
                formatted_result=QLocale().toString(result, 'f', 2)
                if ',' in formatted_result:
                    parts = formatted_result.split(',')
                    if parts[1] and all(c == '0' for c in parts[1]):
                        formatted_result = parts[0] # remove trailing zeros    
                self.lineEdit.setText(formatted_result)
                self.label.setText(f"{textn1} {self.op} {textn2} =")
                self.nm1 = formatted_result
                self.nm2 = None
                self.temp = 0
                self.op = ""
            except ZeroDivisionError:
                self.lineEdit.setText("Zero Division")

    def reset(self):
        self.op=""
        self.nm1=None
        self.nm2=None
        self.temp=0
        self.label.setText('')
        self.lineEdit.setText('0')
    
    def updatefont(self):
        font = self.lineEdit.font()
        font_metrics = QFontMetrics(font)
        text = self.lineEdit.text()
        text_width = font_metrics.width(text)
        widget_widt = self.lineEdit.width()
        MAXIMUM_FONT_SIZE = 35  # tamanho maximo que deseja
        while text_width > widget_widt:
            font.setPointSize(font.pointSize() - 1)
            font_metrics = QFontMetrics(font)
            text_width = font_metrics.width(text)
        else:
            while text_width < widget_widt and font.pointSize() < MAXIMUM_FONT_SIZE:
                font.setPointSize(font.pointSize() + 1)
                font_metrics = QFontMetrics(font)
                text_width = font_metrics.width(text)
        text_width = font_metrics.width(text)
        while text_width > widget_widt:
            font.setPointSize(font.pointSize() - 1)
            font_metrics = QFontMetrics(font)
            text_width = font_metrics.width(text)
        self.lineEdit.setFont(font)

    def delete(self):
        Str=""
        if self.op:
            if len(self.lineEdit.text()) == 1:
                self.lineEdit.setText("0")
                self.temp=0
            else:
                Str = self.lineEdit.text()[:len(self.lineEdit.text())-1]
                self.lineEdit.setText(Str)
            self.nm2=self.lineEdit.text()
        else:
            if len(self.lineEdit.text()) == 1:
                self.lineEdit.setText("0")
                self.temp=0
            else:
                Str = self.lineEdit.text()[:len(self.lineEdit.text())-1]
                self.lineEdit.setText(Str)
            self.nm1=self.lineEdit.text()
        
    def keyPressEvent(self, event):
        numbers_key = [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]
        operations_key = {Qt.Key_Minus: "sub", Qt.Key_Plus:"sum", Qt.Key_Asterisk:"mult", Qt.Key_Slash:"div", Qt.Key_Equal:"result", Qt.Key_Enter:"result", Qt.Key_Return:"result", Qt.Key_Backspace:"del", Qt.Key_Delete:"del", 44:'decimal'}
        if event.key() in numbers_key:
            n = event.key() - Qt.Key_0 #convert the key code to the corresponding number
            button = getattr(self, f"btn{n}")
            button.animateClick()
        elif event.key() in operations_key:
            func=operations_key.get(event.key())
            button = getattr(self, f"btn{func}")
            button.animateClick()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
