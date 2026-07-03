# Learn how to properly structure objects 

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Container Test 1")
		self.setFixedSize(500, 600)
		self.setStyleSheet("background-color: #f7f197")

		# Layout Container
		self.container = QWidget()
		self.layout = QVBoxLayout(self.container)
		self.setCentralWidget(self.container)

		self.vertical_layout()

		self.horizontal_layout()

	def vertical_layout(self):
		self.v_container = QWidget()
		self.v_layout = QVBoxLayout(self.v_container)
		self.v_container.setStyleSheet("background-color: red")

		self.v_container.setFixedSize(300, 200)

		self.layout.addWidget(self.v_container)

		self.V_Buttons()

	def V_Buttons(self):
		self.button1 = QPushButton("1")
		self.button2 = QPushButton("2")
		self.button3 = QPushButton("3")
		self.button4 = QPushButton("4")	

		self.button1.setCursor(Qt.CursorShape.PointingHandCursor)
		self.button2.setCursor(Qt.CursorShape.PointingHandCursor)
		self.button3.setCursor(Qt.CursorShape.PointingHandCursor)
		self.button4.setCursor(Qt.CursorShape.PointingHandCursor)


		self.v_layout.addWidget(self.button1)
		self.v_layout.addWidget(self.button2)
		self.v_layout.addWidget(self.button3)
		self.v_layout.addWidget(self.button4)

		
	def horizontal_layout(self):
		self.v_container = QWidget()
		self.v_layout = QHBoxLayout(self.v_container)
		self.v_container.setStyleSheet("background-color: #03adfc")

		self.v_container.setFixedSize(300, 200)

		self.layout.addWidget(self.v_container)

		self.H_Buttons()


	def H_Buttons(self):
		self.buttonA = QPushButton("A")
		self.buttonB = QPushButton("B")
		self.buttonC = QPushButton("C")
		self.buttonD = QPushButton("D")	

		self.buttonA.setCursor(Qt.CursorShape.PointingHandCursor)
		self.buttonB.setCursor(Qt.CursorShape.PointingHandCursor)
		self.buttonC.setCursor(Qt.CursorShape.PointingHandCursor)
		self.buttonD.setCursor(Qt.CursorShape.PointingHandCursor)

		self.v_layout.addWidget(self.buttonA)
		self.v_layout.addWidget(self.buttonB)
		self.v_layout.addWidget(self.buttonC)
		self.v_layout.addWidget(self.buttonD)

	
app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
