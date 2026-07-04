# Learn how to properly structure objects, containers and layout 

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Container Test 2")
		self.setFixedSize(800, 700)
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
		# Child widget for the label will be a button - DONE
		self.container_one = QWidget()
		self.layout_one = QVBoxLayout(self.container_one)

		self.container_one.setStyleSheet("background-color: green;")
		self.container_one.setFixedSize(300, 300)

		self.layout.addWidget(self.container_one, 0, 0)

		self.Labels()

		self.counter = 0

	def Labels(self):
		self.apple = QLabel("APPLE", self)
		self.banana = QLabel("BANANA", self)
		self.coconut = QLabel("COCONUT", self)

		self.apple_layout = QHBoxLayout(self.apple) # layout using label
		self.apple_layout.setContentsMargins(50, 5, 5, 5)

		self.banana_layout = QHBoxLayout(self.banana)
		self.banana_layout.setContentsMargins(50, 5, 5, 5)
	

		self.coconut_layout = QHBoxLayout(self.coconut)
		self.coconut_layout.setContentsMargins(50, 5, 5, 5)



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

		self.Delete_Button()

		# print(self.apple.parent())

	def Delete_Button(self):
		self.button1 = QPushButton("Delete", self.apple)
		self.button2 = QPushButton("Delete", self.banana)
		self.button3 = QPushButton("Delete", self.coconut)

		self.button1.setFixedSize(100, 30)
		self.button2.setFixedSize(100, 30)
		self.button3.setFixedSize(100, 30)

		self.button1.setStyleSheet("color: black")
		self.button2.setStyleSheet("color: black")
		self.button3.setStyleSheet("color: black")


		self.button1.setCursor(Qt.CursorShape.PointingHandCursor)
		self.button2.setCursor(Qt.CursorShape.PointingHandCursor)
		self.button3.setCursor(Qt.CursorShape.PointingHandCursor)


		# print(self.button1.parent())  # Display the parent of the widget

		self.apple_layout.addWidget(self.button1)
		self.banana_layout.addWidget(self.button2)
		self.coconut_layout.addWidget(self.button3)
	

	def Container_Two(self):
		# Create Button - DONE
		# Each time button is pressed, number inside button is changed - DONE
		# Each time button is pressed, label of number is created on each row - DONE
		# Each label will have a delete button as child

		self.container_two = QWidget()
		self.layout_two = QVBoxLayout(self.container_two)

		self.container_two.setStyleSheet("background-color: #fffb91;")
		self.container_two.setFixedSize(300, 300)

		self.layout.addWidget(self.container_two, 0, 1)

		self.Increment_Button()

	def Increment_Button(self):
			self.numButton = QPushButton("", self.container_two)

			self.numButton.setFixedSize(100, 50)
			self.numButton.setCursor(Qt.CursorShape.PointingHandCursor)

			self.layout_two.addWidget(self.numButton, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

			self.numButton.clicked.connect(self.Display_Number)

	def Display_Number(self):
		self.counter += 1
		self.numLabel = QLabel(str(self.counter), self.container_two)
		self.numLabel_layout = QHBoxLayout(self.numLabel)

		if self.counter >= 6:
			self.numButton.setText("")
			self.counter = 0 
			self.numButton.clicked.disconnect(self.Display_Number)
		else:
			self.numButton.setText(str(self.counter))
			self.layout_two.addWidget(self.numLabel)
			self.Number_Delete_Button()

	def Number_Delete_Button(self):
		self.delete = QPushButton("Delete")
		self.delete.setFixedSize(100, 30)
	
		self.delete.setCursor(Qt.CursorShape.PointingHandCursor)

		self.numLabel_layout.addWidget(self.delete)		
		self.delete.clicked.connect(self.delete_handler)

	def delete_handler(self):
		delete_signal = self.sender()

	def Container_Three(self):
		self.container_three = QWidget()
		self.layout_three = QVBoxLayout(self.container_three)

		self.container_three.setStyleSheet("background-color: pink;")
		self.container_three.setFixedSize(300, 300)

		self.layout.addWidget(self.container_three, 1, 0)


	def Container_Four(self):
		self.container_four = QWidget()
		self.layout_four = QVBoxLayout(self.container_four)

		self.container_four.setStyleSheet("background-color: #91fffb;")
		self.container_four.setFixedSize(300, 300)

		self.layout.addWidget(self.container_four, 1, 1)


app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
