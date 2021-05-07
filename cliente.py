import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    # Criando uma Janela
    def __init__(self):
        super().__init__()
        self.title = 'Cliente P1'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        # Janela
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Interface
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        

        #Renderizar
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())