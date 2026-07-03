# Learn how to properly structure objects, containers and layout 

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Container Test 2")
		self.setFixedSize(500, 600)
		self.setStyleSheet("background-color: #dbdbdb")

		# Layout Container
		self.container = QWidget()
		self.layout = QVBoxLayout(self.container)
		self.setCentralWidget(self.container)

		self.Container_One()
		self.Container_Two()
		self.Container_Three()
		self.Container_Four()

	def Container_One(self):
		# Vertical Layout
		# QLabel
		# Child widget for the label will be a button
		pass

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
