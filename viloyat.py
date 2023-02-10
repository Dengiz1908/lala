from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QMainWindow
from PyQt5.QtWidgets import QComboBox,QLabel,QMessageBox,QCheckBox,QRadioButton
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    andijon = ["","Andijon shahri","Andijon tumani","Asaka tumani","Baliqchi tumani","Bo'z tumani","Buloqboshi tumani","Izboskan tumani","Jalolquduq tumani","Marhamat tumani","Oltinko'l tumani","Paxtaobod tumani","Qo'rg'ontepa tumani","Shahrixon tumani","Ulug'nor tumani","Xo'jaobod tumani","Xonobod shahri"]
    listb = ["", "Kogon","Olot","Gijduvon","Qorako'l","Jondor"]
    listJ = ["", "Zomin","Arnasoy","Gallaorol"]
    listF = ["", "Bag'dod","Beshariq","Furqat","Oltiariq","Rishton"]
    listNam = ["", "Chortoq","Chust","Kosonsoy","Norin","Pop"]
    listSur = ["", "Termiz","Denov","Sherobod","Sho'rchi","Boysun"]
    listSir = ["", "Guliston","Boyovut","Hovos","Oqoltin","Mirzobod"]
    listN = ["", "Navoiy","Xatirchi","Qiziltepa","Tomdi","Nurota"]
    listQ = ["", "Kitob","Qarshi","Yakkasaroy","Yakkabog'","Chiroqchi"]
    listX = ["", "Xonqa","Bog'ot","Xiva","Urganch"]
    listT = ["", "Toshkent","Yashnobod","Mirzo Ulug'bek","Chirchiq","Yunusobod"]
    listSam = ["", "Samarqand","Chimboy","Chelak","Narpay","Toyloq"]
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")
        self.setGeometry(100,100,800,950)
        self.start1()
    def start1(self):
        self.savol=QLabel("Rayhon milliy taomlar restaraniga xush kelibsiz!",self)
        self.savol.setFont(QFont("Times",20))
        self.savol.move(150,50)

        self.savol2=QLabel(" 1-Taom uchun ",self)
        self.savol2.setFont(QFont("Times",20))
        self.savol2.move(50,80)

        self.v1=QCheckBox("Osh",self)
        self.v1.setFont(QFont("Times",20))
        self.v1.move(100,100)

        self.v2=QCheckBox("Manti",self)
        self.v2.setFont(QFont("Times",20))
        self.v2.move(100,150)

        self.v3=QCheckBox("Honim",self)
        self.v3.setFont(QFont("Times",20))
        self.v3.move(100,200)

        self.v4=QCheckBox("Shashlik",self)
        self.v4.setFont(QFont("Times",20))
        self.v4.move(100,250)

        self.savol3=QLabel(" 2-Taom uchun ",self)
        self.savol3.setFont(QFont("Times",20))
        self.savol3.move(50,300)

        self.s1=QCheckBox("Chuchvara",self)
        self.s1.setFont(QFont("Times",20))
        self.s1.move(100,320)

        self.s2=QCheckBox("Sho'rva",self)
        self.s2.setFont(QFont("Times",20))
        self.s2.move(100,370)

        self.s3=QCheckBox("Baliq",self)
        self.s3.setFont(QFont("Times",20))
        self.s3.move(100,420)

        self.s4=QCheckBox("So'msa",self)
        self.s4.setFont(QFont("Times",20))
        self.s4.move(100,470)

        self.combo=QComboBox(self)
        self.combo.addItems(["1","2","3","4"])
        self.combo.setFont(QFont("Times",20))
        self.combo.move(250,100)

        self.combo2=QComboBox(self)
        self.combo2.addItems(["1","2","3","4"])
        self.combo2.setFont(QFont("Times",20))
        self.combo2.move(250,150)

        self.combo3=QComboBox(self)
        self.combo3.addItems(["1","2","3","4"])
        self.combo3.setFont(QFont("Times",20))
        self.combo3.move(250,200)

        self.combo4=QComboBox(self)
        self.combo4.addItems(["1","2","3","4"])
        self.combo4.setFont(QFont("Times",20))
        self.combo4.move(250,250)

        ok=QPushButton("OK",self)
        ok.setFont(QFont("Times",20))
        ok.move(100,400)
        ok.clicked.connect(self.run)

    def run(self):
        win=QMessageBox(self)
        win.setFont(QFont("Times",20))
        if self.v1.isChecked():
            self.v1*self.combo.currentText()
            win.show()
        else:
            win.setText("Siz "+self.combo.currentText()+" yo'nalishini tanladingiz")
            win.show()
win=Window()
win.show()
sys.exit(app.exec_())