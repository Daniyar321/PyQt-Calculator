from PyQt5 import QtCore, QtGui, QtWidgets
from calcul import Ui_MainWindow
import sys
    
#основная логика калькулятора
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.btnClicked)
        
    def btnClicked(self):
        numbers=1
        self.ui.lcdNumber.display(numbers)
        
    

#создание приложения
app = QtWidgets.QApplication([])

#создание формы и инициализация Ui
application = mywindow()
application.show()

#чтение главного цикла
sys.exit(app.exec())
    
