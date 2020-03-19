from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox

from pad import Pad, Aliens, Sd


app = QtWidgets.QApplication(sys.argv)
class ExampleWindow(QMainWindow): #класс окна
	
	def __init__(self):
		super().__init__()
		self.setMinimumSize(QSize(800, 600))
		self.setWindowTitle('Пришельцы')
		central_widget = QWidget(self)
		self.alien_timer = QBasicTimer() #таймер
		self.setCentralWidget(central_widget)
		self.sd = Sd(QtWidgets.QLabel(self), 'sd.png', 400, 550) #создаем экземпляр класса Sd с атрибутами (obj, pic_name, x, y) где obj? это лэйбл
		self.pad_l = Pad(QtWidgets.QLabel(self), 'pad.png', 10, 550) #создаем экземпляр класса Pad с атрибутами (obj, pic_name, x, y) где obj? это лэйбл
		self.numbers = 30
		self.aliens_labl = [] # создаем список и заполняем его лейбами
		for i in range(self.numbers):
			self.aliens_labl.append(QtWidgets.QLabel(self))

		self.al = Aliens(self.aliens_labl, 'alien.png') #создаем экземпляр класса Aliens с атрибутами списка состоящего из лейб
		self.alien_timer.start(100, self)	#запускаем таймер


	def keyPressEvent(self, event):	

		if event.key() == QtCore.Qt.Key_D:
			self.pad_l.move(10)	# запускаем экземпляр класса Pad, его метод move, с атрибутом pad_step равным 10 
		if event.key() == QtCore.Qt.Key_A:
			self.pad_l.move(-10)	
		if event.key() == QtCore.Qt.Key_S and self.sd.y == 540: # условие, чтобы не отстреливать всех пришельцев подряд
			self.sd.move() # запускаем метод, в котором содержится только совершение выстрела

	def dialogs(self): # метод диалоговых окон

		if len(self.al.aliens) == 0: # если в списке пришельцев не осталось
			self.gameover = QMessageBox.question(main_window, 'конец игры !!!!!!', 'победа \n попробовать снова?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if self.gameover == QMessageBox.Yes:					
				self.al = Aliens(self.aliens_labl, 'alien.png')	 # презапуск класса с пришельцами
			else:
				sys.exit(app.exec_())
		
		if self.al.aliens[len(self.al.aliens)-1].y >= 550: # если координаты по y последнего (в списке) прешельца больше чем 550
			self.gameover = QMessageBox.question(main_window, 'конец игры !!!!!!', 'пришельцы нас захватили \n попробовать снова?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if self.gameover == QMessageBox.Yes:					
				self.al = Aliens(self.aliens_labl, 'alien.png')	# презапуск класса с пришельцами				
			else:
				sys.exit(app.exec_())		

	def timerEvent(self, e):
		self.dialogs() # запускаем метод диалогов
		self.al.tic() # запускаем пришельцев
		self.sd.tic(10, self.pad_l.x, self.pad_l.y) # первый атрибут определяет скорость выстрела
		self.sd.shoot(self.al.aliens) # проверяем совпадение sd и пришельца
		
	


		


#app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()
main_window.show()	
sys.exit(app.exec_())
