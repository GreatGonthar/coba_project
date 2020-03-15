from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget

from pad import Pad, Aliens, Sd


class ExampleWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(QSize(800, 600))
		self.setWindowTitle('Пришельцы')
		central_widget = QWidget(self)
		self.alien_timer = QBasicTimer()
		self.setCentralWidget(central_widget)
		self.sd = Sd(QtWidgets.QLabel(self), 'sd.png', 10, 550)


		self.pad_l = Pad(QtWidgets.QLabel(self), 'pad.png', 10, 550)
	
		self.aliens_labl = []
		for i in range(28):
			self.aliens_labl.append(QtWidgets.QLabel(self))

		self.al = Aliens(self.aliens_labl, 'alien.png')
		self.alien_timer.start(100, self)	


	def keyPressEvent(self, event):	

		if event.key() == QtCore.Qt.Key_D:
			self.pad_l.move(10)	
		if event.key() == QtCore.Qt.Key_A:
			self.pad_l.move(-10)	
		if event.key() == QtCore.Qt.Key_S:
			self.sd.move(self.pad_l.pad_x, self.pad_l.pad_y)
			

	def timerEvent(self, e):
		self.al.tic()
		self.sd.tic()


app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()
main_window.show()	
sys.exit(app.exec_())
