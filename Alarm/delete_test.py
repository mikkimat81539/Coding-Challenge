# Every button click will create  a label that increments by 1
# Each label will be in same column but different row
# Each label will have a delete button
# I will store each number in a sorteed list (database)

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Delete Test")
		self.setFixedSize(500, 600)
		self.setStyleSheet("background-color: pink")

		# Layout Container
		self.container = QWidget()
		self.layout = QGridLayout(self.container)
		self.setCentralWidget(self.container)

		# Button Counter
		self.counter = 0

		self.database = sorted([]) # This is for storing the numbers

		# Label Index
		self.rowIndex = 2


	def Label(self):
		self.numLabel = QLabel("")
		self.numLabel.setStyleSheet("""
			font-size: 20px;
			color: black;
		""")

		self.layout.addWidget(self.numLabel, self.rowIndex, 0)

	def Increment_Button(self):
		self.button = QPushButton("")
		self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.button.setFixedSize(100, 50)

		self.layout.addWidget(self.button, 0, 0)

		self.button.clicked.connect(self.button_clicked)

	def Delete_Button(self):
		self.delete_button = QPushButton("Delete")
		self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.delete_button.setFixedSize(100, 30)

		self.layout.addWidget(self.delete_button, self.rowIndex, 1)

	def button_clicked(self):
		self.Label()
		self.Delete_Button()
		self.counter += 1
		self.button.setText(str(self.counter))

		self.numLabel.setText(str(self.counter))
		self.rowIndex += 1

		self.database.append(self.counter)


app = QApplication([])

screen = MainWindow()

screen.Increment_Button()

screen.show()

app.exec()
