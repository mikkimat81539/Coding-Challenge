# Learn how to properly structure objects, containers and layout 

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Container Test 2")
		self.setFixedSize(800, 600)
		self.setStyleSheet("background-color: #dbdbdb")

		# Layout Container
		self.container = QWidget()
		self.layout = QGridLayout(self.container)
		self.setCentralWidget(self.container)

		self.Container_One()
		self.Container_Two()
		self.Container_Three()
		self.Container_Four()

	def Container_One(self):
		# Vertical Layout - DONE
		# QLabel - DONE
		# Child widget for the label will be a button
		self.container_one = QWidget()
		self.layout_one = QVBoxLayout(self.container_one)

		self.container_one.setStyleSheet("background-color: green;")
		self.container_one.setFixedSize(300, 300)

		self.layout.addWidget(self.container_one, 0, 0)

		self.Label_Button()

	def Label_Button(self):
		self.apple = QLabel("APPLE")
		self.banana = QLabel("BANANA")
		self.coconut = QLabel("COCONUT")

#		self.apple.setAlignment(Qt.AlignmentFlag.AlignCenter)
#		self.banana.setAlignment(Qt.AlignmentFlag.AlignCenter)	
#		self.coconut.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.apple.setStyleSheet("""
			font-size: 20px;
			color: red;
		""")

		self.banana.setStyleSheet("""
			font-size: 20px;
			color: yellow;
		""")


		self.coconut.setStyleSheet("""
			font-size: 20px;
			color: white;
		""")


		self.layout_one.addWidget(self.apple)
		self.layout_one.addWidget(self.banana)
		self.layout_one.addWidget(self.coconut)

	def Container_Two(self):
		pass

	def Container_Three(self):
		pass

	def Container_Four(self):
		pass

app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
