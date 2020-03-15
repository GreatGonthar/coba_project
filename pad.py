from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget


class Pad():
	def __init__(self):
		self.pad_x = 10
		self.pad_y = 550
		self.pad_width = 50
		self.pad_height = 50
		self.window_width = 800
		self.obj = 0

	def init(self,obj,pic_name,x,y):
		self.pad_x = x
		self.pad_y = y
		print('hallo',pic_name )
		self.obj = obj
		self.obj.setGeometry(QtCore.QRect(self.pad_x, self.pad_y, self.pad_width, self.pad_height))
		self.obj.setPixmap(QtGui.QPixmap(pic_name))	

	def move(self, pad_step):
		new_pad_x = self.pad_x + pad_step
		if new_pad_x + self.pad_width >= self.window_width:
			return False
		if new_pad_x <= 0: 
			return False
		self.pad_x = new_pad_x

		self.obj.move(self.pad_x,self.pad_y)
		print(new_pad_x)

