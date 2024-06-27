import sys
from PyQt5.QtWidgets import QApplication
from calculator import Calculator_interface

app = QApplication(sys.argv)
calculator = Calculator_interface()
sys.exit(app.exec_())
