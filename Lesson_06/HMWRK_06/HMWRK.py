import time
import threading
import curses

""" Базовый класс для таймера """

class TimerBase:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.is_running = False

    # Метод для запуска таймера
    def start(self):
        self.reset()  # Всегда обнуляем таймер перед стартом
        self.start_time = time.time()
        self.is_running = True

    # Метод для сброса таймера
    def reset(self):
        self.start_time = None
        self.paused_time = 0
        self.is_running = False

    # Метод для приостановки таймера
    def pause(self):
        if self.is_running:
            self.paused_time = self.elapsed_time()
            self.is_running = False

    # Метод для возобновления таймера после паузы
    def resume(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True

    # Метод для получения текущего времени, учитывая паузу
    def elapsed_time(self):
        if self.is_running:
            return time.time() - self.start_time + self.paused_time
        else:
            return self.paused_time

""" Класс для таймера с текстовым интерфейсом в консоли """

class ConsoleTimer(TimerBase):
    def __init__(self, screen):
        super().__init__()
        self.lock = threading.Lock()
        self.screen = screen

    # Метод для обновления текстового интерфейса
    def update_display(self):
        while True:
            with self.lock:
                self.screen.clear()
                self.screen.addstr(f"Прошло времени: {self.elapsed_time():.2f} секунд.\n")
                self.screen.addstr("Введите команду,\n нажав на кнопку:\n")
                self.screen.addstr("1. Запустить\n")
                self.screen.addstr("2. Приостановить\n")
                self.screen.addstr("3. Возобновить\n")
                self.screen.addstr("4. Остановить\n")
                self.screen.addstr("5. Выход\n")
                self.screen.refresh()
                time.sleep(0.09) # Задержка позволяет управлять частотой обновления интерфейса и снижает нагрузку на процессор.

    # Метод для получения команд пользователя
    def get_user_input(self):
        while True:
            key = self.screen.getch()
            if key == ord('1'):
                self.start()
            elif key == ord('2'):
                self.pause()
            elif key == ord('3'):
                self.resume()
            elif key == ord('4'):
                self.reset()
            elif key == ord('5'):
                break

    # Метод для запуска таймера с текстовым интерфейсом
    def run(self):
        curses.curs_set(0)  # Скрыть курсор

        # Создаем поток для обновления текстового интерфейса
        update_thread = threading.Thread(target=self.update_display)
        update_thread.daemon = True
        update_thread.start()
    
        # Создаем поток для получения команд пользователя
        input_thread = threading.Thread(target=self.get_user_input)
        input_thread.daemon = True
        input_thread.start()

        input_thread.join()  # Ждать завершения ввода

""" Запуск """

if __name__ == "__main__":
    # Создаем экземпляр базового таймера для учета времени в приложении.
    base_timer = TimerBase()
    base_timer.start()

    # Используем curses.wrapper для инициализации curses-сессии и передачи объекта экрана (screen)
    curses.wrapper(lambda screen: ConsoleTimer(screen).run())

    print(f"Вы использовали таймер: {base_timer.elapsed_time():.2f} секунд.")
    # Выводим сообщение о временем, которое вы провели в приложении.
