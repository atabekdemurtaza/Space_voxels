import pygame as pg 

RES = WIDTH, HEIGHT = 1600, 900   #разрешение 1600х900 

class App:

	def __init__(self) -> None:
		
		self.screen = pg.display.set_mode(RES) #Создаем поверхность отрисовки
		self.clock  = pg.time.Clock() #Создаем экземпляр Clock для установки FPS 

	def run(self):

		while True: #На каждой итерации выполняем следующее 
			self.screen.fill('black') #закрашиваем поверхность отрисовки в черный цвет 
			
			pg.display.flip() #обновляем кадр(отображаем то что нарисовали на текущей итерации)
			[exit() for i in pg.event.get() if i.type == pg.QUIT] #проверка на закрытие приложения 
			self.clock.tick(60) #устанавливаем 60 кадров в секудну

if __name__ == '__main__':

	app = App() #создаем экземпляр класса App 
	app.run()
