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
        self.op=""
        self.nm1=None
        self.nm2=None
        self.temp=0
        self.negative=""
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("^-?\d+$[0-9]*"),self.lineEdit))
        self.signal.connect(self.sinal)
        self.btn1.clicked.connect(self.btt1)
        self.btn2.clicked.connect(self.btt2)
        self.btn3.clicked.connect(self.btt3)
        self.btn4.clicked.connect(self.btt4)
        self.btn5.clicked.connect(self.btt5)
        self.btn6.clicked.connect(self.btt6)
        self.btn7.clicked.connect(self.btt7)
        self.btn8.clicked.connect(self.btt8)
        self.btn9.clicked.connect(self.btt9)
        self.btn0.clicked.connect(self.btt0)
        self.btndel.clicked.connect(self.bttdel)
        self.btnreset.clicked.connect(self.reset)
        self.btnsum.clicked.connect(self.bttsum)
        self.btnsub.clicked.connect(self.bttsub)
        self.btnresult.clicked.connect(self.result)

    def btt1(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('1')
                self.temp=1
            else:
                self.lineEdit.setText(text+"1")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0 or self.negative=='s':
                self.lineEdit.setText('1')
                self.temp=1
            else:
                self.lineEdit.setText(text+"1")
            self.nm1=self.lineEdit.text()
            return
        
    def btt2(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('2')
                self.temp=1
            else:
                self.lineEdit.setText(text+"2")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('2')
                self.temp=1
            else:
                self.lineEdit.setText(text+"2")
            self.nm1=self.lineEdit.text()
            return

    def btt3(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('3')
                self.temp=1
            else:
                self.lineEdit.setText(text+"3")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('3')
                self.temp=1
            else:
                self.lineEdit.setText(text+"3")
            self.nm1=self.lineEdit.text()
            return
    
    def btt4(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('4')
                self.temp=1
            else:
                self.lineEdit.setText(text+"4")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('4')
                self.temp=1
            else:
                self.lineEdit.setText(text+"4")
            self.nm1=self.lineEdit.text()
            return

    def btt5(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('5')
                self.temp=1
            else:
                self.lineEdit.setText(text+"5")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('5')
                self.temp=1
            else:
                self.lineEdit.setText(text+"5")
            self.nm1=self.lineEdit.text()
            return

    def btt6(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('6')
                self.temp=1
            else:
                self.lineEdit.setText(text+"6")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('6')
                self.temp=1
            else:
                self.lineEdit.setText(text+"6")
            self.nm1=self.lineEdit.text()
            return

    def btt7(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('7')
                self.temp=1
            else:
                self.lineEdit.setText(text+"7")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('7')
                self.temp=1
            else:
                self.lineEdit.setText(text+"7")
            self.nm1=self.lineEdit.text()
            return

    def btt8(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('8')
                self.temp=1
            else:
                self.lineEdit.setText(text+"8")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('8')
                self.temp=1
            else:
                self.lineEdit.setText(text+"8")
            self.nm1=self.lineEdit.text()
            return
            
    def btt9(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('9')
                self.temp=1
            else:
                self.lineEdit.setText(text+"9")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('9')
                self.temp=1
            else:
                self.lineEdit.setText(text+"9")
            self.nm1=self.lineEdit.text()
            return
 
    def btt0(self,event):
        text=self.lineEdit.text()
        if self.op:
            if self.temp==0:
                self.lineEdit.setText('0')
                self.temp=1
            else:
                self.lineEdit.setText(text+"0")
            self.nm2=self.lineEdit.text()
            return
        else:
            if self.temp==0:
                self.lineEdit.setText('0')
                self.temp=1
            else:
                self.lineEdit.setText(text+"0")
            self.nm1=self.lineEdit.text()
            return

    def bttdel(self,event):
        self.signal.emit("del")

    def reset(self,event):
        self.signal.emit("reset")

    def bttsum(self,event):
        if self.op and self.nm2 and self.nm1:
            if self.op=="-":
                self.signal.emit('--')
                return
            if self.op=="+":
                self.signal.emit('+1')
                return
        if self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op="+"
            self.temp=0
            self.label.setText(self.nm1+" +")
            return
        if self.nm1:
            self.op="+"
            self.temp=0
            self.label.setText(self.nm1+" +")

    def bttsub(self,event):
        if self.op and self.nm2 and self.nm1:
            if self.op=="-":
                self.signal.emit('-1')
                return
            if self.op=="+":
                self.signal.emit('++')
                return
        if self.nm1 and self.negative=='s':
            self.negative=""
            self.nm1=str(int(self.nm1)*-1)
            self.op="-"
            self.temp=0
            self.label.setText(self.nm1+" -")
            return
        if self.nm1:
            self.op="-"
            self.temp=0
            self.label.setText(self.nm1+" -")
            return
        if self.lineEdit.text()=="0":
            self.negative="s"
            self.label.setText("0 -")
       
    def result(self,event):
        self.signal.emit(self.op)

    def sinal(self,response):
        print(response)
        if response=="+":
            try:
                result=int(self.nm1)+int(self.nm2)
                self.lineEdit.setText(str(result))
                self.label.setText(self.nm1+" + "+self.nm2+" =")
                self.nm1=None
                self.nm2=None
                self.temp=0
                self.op=''
            except:
                pass
        if response=="+1":
            result=int(self.nm1)+int(self.nm2)
            self.label.setText(str(result)+" +")
            self.lineEdit.setText(str(result))
            self.nm1=self.lineEdit.text()
            self.nm2=None
            self.temp=0
        if response=="++":
            result=int(self.nm1)+int(self.nm2)
            self.label.setText(str(result)+" -")
            self.lineEdit.setText(str(result))
            self.nm1=self.lineEdit.text()
            self.nm2=None
            self.temp=0
            self.op='-'
        if response=="-":
            try:
                result=int(self.nm1)-int(self.nm2)
                self.lineEdit.setText(str(result))
                self.label.setText(self.nm1+" - "+self.nm2+" =")
                self.nm1=None
                self.nm2=None
                self.temp=0
                self.op=''
            except:
                pass
        if response=="-1":
            result=int(self.nm1)-int(self.nm2)
            self.label.setText(str(result)+" -")
            self.lineEdit.setText(str(result))
            self.nm1=self.lineEdit.text()
            self.nm2=None
            self.temp=0
        if response=="--":
            if int(self.nm2)>int(self.nm1) and int(self.nm1)>0:
                result=(int(self.nm2)-int(self.nm1))*-1
            elif int(self.nm2)>0 and int(self.nm1)<0 and self.op=="+":
                result=int(self.nm2)+int(self.nm1)
            else:
                result=int(self.nm1)-int(self.nm2)
            self.label.setText(str(result)+" +")
            self.lineEdit.setText(str(result))
            self.nm1=self.lineEdit.text()
            self.nm2=None
            self.temp=0
            self.op="+"
        if response=="reset":
            self.op=""
            self.nm1=None
            self.nm2=None
            self.temp=0
            self.label.setText('')
            self.lineEdit.setText('0')
        if response=="del":
            if len(self.lineEdit.text()) == 1:
                self.lineEdit.setText("0")
                self.temp=0
            else:
                Str = self.lineEdit.text()[:len(self.lineEdit.text())-1]
                self.lineEdit.setText(Str)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
