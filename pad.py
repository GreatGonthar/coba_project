from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget

class Pad():
	def __init__(self, obj, pic_name, x, y):

		self.pad_width = 50
		self.pad_height = 50
		self.window_width = 800
		self.pad_x = x
		self.pad_y = y
		self.obj = obj
		self.obj.setGeometry(QtCore.QRect(self.pad_x, self.pad_y, self.pad_width, self.pad_height))
		self.setPixel(pic_name)

	def setPixel(self, pic_name):
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

class Alien():		
	def __init__(self, QLabel, pic_name, x, y):
		self.x = x
		self.y = y
		self.width = 50
		self.height = 50
		self.obj = QLabel
		self.obj.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))
		self.obj.setPixmap(QtGui.QPixmap(pic_name))		

	def move(self, x, y):
		self.x = x
		self.y = y
		self.obj.move(self.x,self.y)

class Aliens():		
	def __init__(self, alien_obj, pic_name):		
		self.alien_obj = alien_obj
		self.aliens = []
		self.a = len(self.alien_obj)
		self.step = 10
		self.window_width = 800
		
		y = 10
		for i in range(self.a):
			i2=i%10	
			x = i2 * (50+10)
			if i2 == 0:
				x = 1
				y += 60			
			self.aliens.append(Alien(self.alien_obj[i], pic_name ,x , y))

	def tic(self):
		min_x = self.aliens[0].x
		max_x = self.aliens[0].x+self.aliens[0].width
		max_y = self.aliens[0].y+self.aliens[0].height

		for i in self.aliens:
			if(min_x>i.x):
				min_x=i.x
			if(max_x<i.x+i.width):
				max_x=i.x+i.width
			if(max_y<i.y+i.height):
				max_y=i.y+i.height

		diff_y=0	
		if max_x >= self.window_width or min_x <= 0:
			self.step = -self.step
			diff_y = 50

		for i in self.aliens:
			i.move(i.x+self.step,i.y+diff_y) 

class Sd(Pad):
	def setPixel(self, pic_name):
		self.obj.setPixmap(QtGui.QPixmap(pic_name).scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation))
	
	def move(self, x, y):
		self.pad_x = x
		self.pad_y= y
		self.obj.move(self.pad_x,self.pad_y)

	def tic(self):

		self.move(self.pad_x,self.pad_y+1)

		







				