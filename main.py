import pygame 

RES = WIDTH,HEIGHT = 1600, 900 #разрешение 1600х900

class App:

	def __init__(self):

	    self.screen = pygame.display.set_mode(RES) #Создаем поверхность отрисовки
	    self.clock = pygame.time.Clock() #создаем экземпляр Clock для установки FPS

	def run(self):

		while True: #На каждой итерации выполняем следующее:
			self.screen.fill('black') #Закрашиваем поверхность отрисовки в черный цвет

			pygame.display.flip() #обновляем кадр отображаем то, что нарисовали на текущей итерации
			[exit() for i in pygame.event.get() if i.type == pygame.QUIT] #Проверка на закрытые приложения
			self.clock.tick(60) #Устанавливем 60 кадров в секунду

if __name__ == '__main__':

	app = App() #Создаем экземпляр класса App 
	app.run() #вызываем метод Запуск или (run)
	