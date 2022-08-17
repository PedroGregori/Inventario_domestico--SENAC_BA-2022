from PyQt5.QtWidgets import QApplication 
import sys
from controller.main_window import MainWindow

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()