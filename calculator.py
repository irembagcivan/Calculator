from PyQt5 import QtWidgets
from interface import Ui_MainWindow

class Calculator_interface(QtWidgets.QMainWindow,Ui_MainWindow):
    ilk_sayi = None
    ikinci_sayi = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Rakam butonları etkileşimi
        self.pushButton_1.clicked.connect(self.frakam_basma)
        self.pushButton_2.clicked.connect(self.frakam_basma)
        self.pushButton_3.clicked.connect(self.frakam_basma)
        self.pushButton_4.clicked.connect(self.frakam_basma)
        self.pushButton_5.clicked.connect(self.frakam_basma)
        self.pushButton_6.clicked.connect(self.frakam_basma)
        self.pushButton_7.clicked.connect(self.frakam_basma)
        self.pushButton_8.clicked.connect(self.frakam_basma)
        self.pushButton_9.clicked.connect(self.frakam_basma)
        self.pushButton_0.clicked.connect(self.frakam_basma)

        # Nokta butonu etkileşimi
        self.pushButton_nokta.clicked.connect(self.fondalik)

        # İşaret ve yüzde butonu etkileşimi
        self.pushButton_isaret.clicked.connect(self.fisaret_yuzde)
        self.pushButton_yuzde.clicked.connect(self.fisaret_yuzde)
    
        # İşlem operatörleri butonlarının etkileşimi
        self.pushButton_arti.clicked.connect(self.fislem)
        self.pushButton_eksi.clicked.connect(self.fislem)
        self.pushButton_bol.clicked.connect(self.fislem)
        self.pushButton_carp.clicked.connect(self.fislem)

        self.pushButton_arti.setCheckable(True)
        self.pushButton_eksi.setCheckable(True)
        self.pushButton_bol.setCheckable(True)
        self.pushButton_carp.setCheckable(True)

        # Eşittir butonu etkileşimi
        self.pushButton_esittir.clicked.connect(self.fsonuc)
        self.pushButton_esittir.setCheckable(True)

        # Temizle butonu etkileşimi
        self.pushButton_temizle.clicked.connect(self.ftemizle)

    # Herhangi bir rakam butonuna basıldığında çalışacak fonksiyon
    def frakam_basma(self):
        buton = self.sender() # Hangi nesneye basıldığını gösterir

        if((self.ikinci_sayi) and (self.pushButton_esittir.isChecked())):
            self.label.setText(format(float(buton.text()),"15g"))
            self.ikinci_sayi = True
            self.pushButton_esittir.setChecked(False)

        elif ((self.pushButton_arti.isChecked() or self.pushButton_eksi.isChecked() or self.pushButton_bol.isChecked() or self.pushButton_carp.isChecked()) and (not self.ikinci_sayi)):
            self.label.setText(format(float(buton.text()),".15g"))
            self.ikinci_sayi = True
        else:
            if(("." in self.label.text()) and buton.text() == "0"):
                self.label.setText(format(float(self.label.text() + buton.text()),".15")) 
            else:
                self.label.setText(format(float(self.label.text() + buton.text()),".15g"))
    
    # Virgüllü sayıları tanımlama
    def fondalik(self):
        if "." not in self.label.text():
            self.label.setText(self.label.text() + ".")
    
    def fisaret_yuzde(self):
        buton = self.sender()
        deger = float(self.label.text())

        if buton.text() == "+/-":
            deger = deger * -1
        else:
            deger = deger * 0.01
        
        self.label.setText(format(deger,".15g"))
    
    def fislem(self):
        buton = self.sender()
        self.ilk_sayi = float(self.label.text())
        buton.setChecked(True)
    
    def fsonuc(self):
        ikinci_deger = float(self.label.text())

        if self.pushButton_arti.isChecked():
            yenideger = self.ilk_sayi + ikinci_deger
            self.label.setText(format(yenideger,".15"))
            self.pushButton_arti.setChecked(False)

        elif self.pushButton_eksi.isChecked():
            yenideger = self.ilk_sayi - ikinci_deger
            self.label.setText(format(yenideger,".15"))
            self.pushButton_eksi.setChecked(False)

        elif self.pushButton_carp.isChecked():
            yenideger = self.ilk_sayi * ikinci_deger
            self.label.setText(format(yenideger,".15"))
            self.pushButton_carp.setChecked(False)
            
        elif self.pushButton_bol.isChecked():
            yenideger = self.ilk_sayi / ikinci_deger
            self.label.setText(format(yenideger,".15"))
            self.pushButton_bol.setChecked(False)
    
        self.ilk_sayi = yenideger
        self.pushButton_esittir.setChecked(True)
        
    def ftemizle(self):
        self.ilksayi = 0
        self.ikinci_sayi = False
        self.label.setText("0")
        self.pushButton_arti.setChecked(False)
        self.pushButton_eksi.setChecked(False)
        self.pushButton_carp.setChecked(False)
        self.pushButton_bol.setChecked(False)

