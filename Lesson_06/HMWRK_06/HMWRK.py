import time
import os
import threading

class Timer:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.is_running = False
        self.timer_thread = None
        self.choice = 0 

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.paused_time = 0  # Обнуляем время паузы
            self.is_running = True
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.start()
        else:
            # Если таймер уже запущен, обнуляем его
            self.start_time = time.time()
            self.paused_time = 0

    def pause(self):
        if self.is_running:
            self.paused_time += time.time() - self.start_time
            self.is_running = False

    def resume(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.start()

    def stop(self):
        if self.is_running:
            self.paused_time += time.time() - self.start_time
            self.is_running = False

    def get_elapsed_time(self):
        if self.is_running:
            return self.paused_time + (time.time() - self.start_time)
        else:
            return self.paused_time

    def update_timer(self):
        while self.is_running:
            time.sleep(1)  # Обновление каждую секунду

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')  # Для Windows
        else:
            os.system('clear')  # Для Unix

    def draw_menu(self):
        print("Введите номер действия: ")
        print("1. Запустить секундомер")
        print("2. Приостановить секундомер")
        print("3. Возобновить секундомер")
        print("4. Получить прошедшее время")
        print("5. Выход")

    def draw_timer(self):
        elapsed_time = self.get_elapsed_time()
        print(f"Текущее время: {elapsed_time:.2f} секунд.")
        time.sleep(0.06)  # Ожидание для обновления экрана



# Функция для чтения пользовательского ввода
def user_input(timer):
    while True:
        choice = input(f"{choice}").strip()
        if choice == "1":
            timer.start()
        elif choice == "2":
            timer.pause()
        elif choice == "3":
            timer.resume()
        elif choice == "4":
            print(f"Прошло {timer.get_elapsed_time():.2f} секунд.")
        elif choice == "5":
            timer.stop()
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер действия из списка.")

# Пример использования класса таймера
timer = Timer()

# Создаем поток для пользовательского ввода
input_thread = threading.Thread(target=user_input, args=(timer,))
input_thread.start()

while True:
    timer.clear_screen()
    timer.draw_menu()
    timer.draw_timer()
