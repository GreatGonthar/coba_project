from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget

class Pad():
	def __init__(self, QLabel, pic_name, x, y):

		self.pad_width = 50 #размеры игрока
		self.pad_height = 50
		self.window_width = 800 #ширина окна
		self.x = x #начальные координаты игрока
		self.y = y
		self.obj = QLabel #это наш объект (в данном случае лэйбл)
		self.obj.setGeometry(QtCore.QRect(self.x, self.y, self.pad_width, self.pad_height))  # создаем объект на форме. с координатами
		self.setPixel(pic_name) #?

	def setPixel(self, pic_name):
		self.obj.setPixmap(QtGui.QPixmap(pic_name)) #создаем изображение объекта

	def move(self, pad_step): # движение игрока с атрибутом его шага
		new_x = self.x + pad_step # создаем временную переменную, для обработки выхода игрока за экран
		if new_x + self.pad_width >= self.window_width:
			return False
		if new_x <= 0: 
			return False
		self.x = new_x
		self.obj.move(self.x,self.y) # двигаем объект используя встроенный метод для Qlable, move


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
		self.alien_obj = alien_obj # в этом атрибуте будет список лэйб
		self.aliens = []
		self.a = len(self.alien_obj) #количество наших пришельцев
		self.step = 10
		self.window_width = 800
		
		y = 10
		for i in range(self.a):
			b = i % 10	# создаем временную переменную которая не будет равна нулю, пока i не будет кратна 10
			x = b * (50 + 10) # получаем координату по x наших пришельцев
			if b == 0:
				x = 1
				y += 60	# если их больше десяти в ряду, то сдвигаем вниз по y		
			self.aliens.append(Alien(self.alien_obj[i], pic_name ,x , y)) #добавляем в список четыре атрибута: лейбу, изображение, полученные координаты


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
			self.aliens[10].obj.setPixmap(QtGui.QPixmap('pad.png'))

class Sd():
	def __init__(self, QLabel, pic_name, x, y):
		self.width = 50 #размеры игрока
		self.height = 50
		#self.window_width = 800 #ширина окна
		self.x = x #начальные координаты игрока
		self.y = y
		self.obj = QLabel #это наш объект (в данном случае лэйбл)
		self.obj.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))  # создаем объект на форме. с координатами
		self.setPixel(pic_name) 	
		self.j = False	


	def setPixel(self, pic_name):
		self.obj.setPixmap(QtGui.QPixmap(pic_name).scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation))

	def move(self, x):	
		if self.j == False:
			self.x = x+10
		self.j = True
	
	def tic(self, k):
		if self.j == True: 
			self.y = self.y - k
			self.obj.move(self.x, self.y)
		if self.y <= 0:
			self.j = False
			self.y = 550
		







				