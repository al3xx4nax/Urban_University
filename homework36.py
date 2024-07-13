import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        global day
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        for i in range(enemies):
            enemies -= self.power
            days += 1
            if enemies < 0:
                print(f"{self.name} одержал победу спустя {days - 1} {day}!")
                break
            if days == 1:
                day = "день"
            elif 1 < days < 5:
                day = "дня"
            else:
                day = "дней"
            time.sleep(1)
            print(f"{self.name} сражается {days} {day}, осталось {enemies} воинов.")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
