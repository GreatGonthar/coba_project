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
			b = i % 8	# создаем временную переменную которая не будет равна нулю, пока i не будет кратна 10
			x = b * (50 + 30) # получаем координату по x наших пришельцев
			if b == 0:
				x = 1
				y += 50	# если их больше десяти в ряду, то сдвигаем вниз по y		
			self.aliens.append(Alien(self.alien_obj[i], pic_name ,x , y)) #добавляем в список четыре атрибута: лейбу, изображение, полученные координаты


	def tic(self):
		min_x = self.aliens[0].x
		max_x = self.aliens[0].x+self.aliens[0].width
		max_y = self.aliens[0].y+self.aliens[0].height

		for i in self.aliens:
			if (min_x > i.x):
				min_x=i.x
			if(max_x<i.x+i.width):
				max_x=i.x+i.width
			if(max_y<i.y+i.height):
				max_y=i.y+i.height



		diff_y=0	
		if max_x >= self.window_width or min_x <= 0:
			self.step = -self.step
			diff_y = 5

		for i in self.aliens:
			i.move(i.x+self.step, i.y+diff_y) 



			

class Sd():
	def __init__(self, QLabel, pic_name, x, y):
		self.width = 30
		self.height = 30
		#self.window_width = 800 #ширина окна
		self.x = x #начальные координаты игрока
		self.y = y
		self.obj = QLabel #это наш объект (в данном случае лэйбл)
		self.obj.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))  # создаем объект на форме. с координатами
		self.setPixel(pic_name) 	
		self.j = False	# временная переменная для события выстрела


	def setPixel(self, pic_name):
		self.obj.setPixmap(QtGui.QPixmap(pic_name).scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)) # уменьшаем картинку

	def move(self):	
		self.j = True # совершаем выстрел
	
	def tic(self, k, x, y): # k - это скорость полета выстрела
		if self.j == True: # если выстрел совершен, двигаем sd по y
			self.y = self.y - k
		else:
			self.x = x+10 # если нет, меняем координаты выстрела, на координаты игрока
			self.y = y-10	
		if self.y <= 0:
			self.j = False			
		self.obj.move(self.x, self.y)

	

	def shoot(self, hit):
		for i in range(len(hit)):
			if self.x+25 >= hit[i].x and self.x <= hit[i].x+40 and self.y <= hit[i].y+50 and self.y-30 >= hit[i].y:
		
				#hit[i].obj.setPixmap(QtGui.QPixmap('pad.png'))
				hit[i].obj.setPixmap(QtGui.QPixmap(None))
				del hit[i]
				return 

		

				






				