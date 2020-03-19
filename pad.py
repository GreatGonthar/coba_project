from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox

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


class Alien():	 # класс пришнльца (не будет использован в основной программе)	
	def __init__(self, QLabel, pic_name, x, y):
		self.x = x
		self.y = y
		self.width = 50 # высота, ширина
		self.height = 50
		self.obj = QLabel
		self.obj.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))
		self.obj.setPixmap(QtGui.QPixmap(pic_name))		

	def move(self, x, y):
		self.x = x
		self.y = y
		self.obj.move(self.x,self.y) # двигаем лейбу

class Aliens():		
	def __init__(self, alien_obj, pic_name):		
		self.alien_obj = alien_obj # в этом атрибуте будет список лэйб
		self.aliens = []
		self.a = len(self.alien_obj) #количество наших пришельцев

		self.step = 1
		self.window_width = 800

		
		
		y = 10
		for i in range(self.a):
			b = i % 8	# создаем временную переменную которая не будет равна нулю, пока i не будет кратна 8
			x = b * (50 + 30) # получаем координату по x наших пришельцев где 30 это расстояние между ними
			if b == 0:
				x = 1
				y += 50	# если их больше 8 в ряду, то сдвигаем вниз по y		
			self.aliens.append(Alien(self.alien_obj[i], pic_name ,x , y)) #добавляем в список четыре атрибута: лейбу, изображение, полученные координаты


	def tic(self):

		min_x = self.aliens[0].x # минимальная x координата первого пришельца 
		max_x = self.aliens[0].x+self.aliens[0].width # максимальная x координата первого пришельца + его размер
		max_y = self.aliens[0].y+self.aliens[0].height # тоже же самое но по y

		for i in self.aliens: # итерируем список (где все данные о каждом пришельце)
			if (min_x > i.x): # если минимальный больше итерируемого в данный момент, то минимальный теперь будет вот этим
				min_x=i.x
			if(max_x<i.x+i.width): # то же и для других
				max_x=i.x+i.width
			if(max_y<i.y+i.height):
				max_y=i.y+i.height

		diff_y=0	# временная переменная для сдвига по y
		if max_x >= self.window_width or min_x <= 0: # условия при ударе об стены
			diff_y += 10 # сдвигаем вниз по y 				
			self.step = -self.step # и меняем направление движения

		for i in self.aliens:
			i.move(i.x+self.step, i.y+diff_y) # меняем координаты на один шаг

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
		if self.y <= 0: # если промахнулись, то событие выстрела делаем не произошедшим, и меняем координаты sd на координаты игрока
			self.j = False			
		self.obj.move(self.x, self.y)	

	def shoot(self, hit):
		for i in range(len(hit)):
			if self.x+25 >= hit[i].x and self.x <= hit[i].x+40 and self.y <= hit[i].y+50 and self.y-30 >= hit[i].y: #если координаты sd совпали с координатой пришельца
				
				#hit[i].obj.setPixmap(QtGui.QPixmap('pad.png'))

				self.j = False		# делаем выстрел не действительным

				hit[i].obj.setPixmap(QtGui.QPixmap(None)) # убираем изображение пришельца
				del hit[i] # удаляем из списка вообще все данные прицельца (включая сам элемент списка)
				return # заканчиваем цыкл



				






				