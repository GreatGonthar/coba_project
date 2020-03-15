from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget


from pad import Pad 


class ExampleWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(QSize(800, 600))
		self.setWindowTitle('Пришельцы')
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)
		self.pad_l = Pad()
		self.pad_obj = QtWidgets.QLabel(self)

	def pad_show(self):
		#self.obj.setGeometry(QtCore.QRect(10, 10, 50, 50))
		#self.obj.setPixmap(QtGui.QPixmap('pad.png'))	
		self.pad_l.init(self.pad_obj,'pad.png', 50, 5)


	def keyPressEvent(self, event):	

		if event.key() == QtCore.Qt.Key_D:
			self.pad_l.move(10)	
		if event.key() == QtCore.Qt.Key_A:
			self.pad_l.move(-10)	
		if event.key() == QtCore.Qt.Key_S:
			pass


app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()
main_window.show()	
main_window.pad_show()
sys.exit(app.exec_())
