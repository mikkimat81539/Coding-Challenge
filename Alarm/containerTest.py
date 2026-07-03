# Learn how to properly structure objects 

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Delete Test")
		self.setFixedSize(500, 600)
		self.setStyleSheet("background-color: #f7f197")

		# Layout Container
		self.container = QWidget()
		self.layout = QGridLayout(self.container)
		self.setCentralWidget(self.container)

	
app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
