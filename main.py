import pygame as pg 
import random 
import math 

vec2, vec3 = pg.math.Vector2, pg.math.Vector3 #Создаем вектора

RES = WIDTH, HEIGHT = 1600, 900   #разрешение 1600х900 
NUM_STARS = 100 #число звезд
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = '#e74645 #1ac0c6 #8a2be2 #f2e968 #c91060 #dee0e6'.split()
Z_DISTANCE = 40 #Создаем 3д (z) где звезды начнут двигатся 



class Star: #Создаем 1 звездочку 

	def __init__(self, app):

		self.screen = app.screen #Поверхность отрисовки 
		self.pos3d  = self.get_pos3d()       #Позиция 3х пространстве 
		self.vel 	= random.uniform(0.05, 0.25) #скорость звезды
		self.color	= random.choice(COLORS) #рандомность цвета
		self.screen_pos = vec2(0, 0) #позиция звезды на экране
		self.size = 10
	
	def get_pos3d(self):

		angle = random.uniform(0, 2*math.pi) #
		radius = random.randrange(HEIGHT)
		#Вычитываем координаты с помощью синуса и косинуса
		x = radius * math.sin(angle)
		y = radius * math.cos(angle)
		return vec3(x, y, Z_DISTANCE) #возвращаем в вектор

	def update(self):

		self.pos3d.z -= self.vel #Будем двигать звезду по оси Z 
		self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d #Если звезда сближается к 1 до рандомно назад
		self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER

	def draw(self):

		pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size)) #Как квадрат

class StarField: #Управляем звезд

	def __init__(self, app):

		self.stars = [Star(app) for i in range(NUM_STARS)]
	
	def run(self):

		[star.update() for star in self.stars]
		[star.draw() for star in self.stars]

class App:

	def __init__(self):
		
		self.screen = pg.display.set_mode(RES) #Создаем поверхность отрисовки
		self.clock  = pg.time.Clock() #Создаем экземпляр Clock для установки FPS 
		self.starfield = StarField(self) 


	def run(self):

		while True: #На каждой итерации выполняем следующее 
			self.screen.fill('black') #закрашиваем поверхность отрисовки в черный цвет 
			self.starfield.run()

			
			pg.display.flip() #обновляем кадр(отображаем то что нарисовали на текущей итерации)
			[exit() for i in pg.event.get() if i.type == pg.QUIT] #проверка на закрытие приложения 
			self.clock.tick(60) #устанавливаем 60 кадров в секудну

if __name__ == '__main__':

	app = App() #создаем экземпляр класса App 
	app.run()
