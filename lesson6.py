# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
#    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __colors_sequence = {"красный": 7, "желтый": 2, "зеленый": 4}
    __check_list = list(__colors_sequence.keys())
    __color = "красный"

    def running(self, new_color):
        print("Новый цвет: {}".format(new_color))
        if new_color in self.__colors_sequence.keys():
            if self.__check_list.index(self.__color) == (self.__check_list.index(new_color) - 1 if self.__check_list.index(new_color) - 1 >= 0 else 0):
                print("Светим цветом '{}' ровно {} секунд".format(new_color, self.__colors_sequence.get(new_color)))
                time.sleep(self.__colors_sequence.get(new_color))
                self.__color = new_color
            else:
                print("нарушение порядка режимов")
        else:
            print("Нет такого света у светофора")


a = TrafficLight()

a.running("зеленый")
a.running("красный")
a.running("зеленый")
a.running("желтый")
a.running("красный")
a.running("зеленый")
print("Готово")


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
#    Проверить работу метода.
#    Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    _length: 0
    _width: 0

    def calc_mass(self, weight_of_one_sm, amount_of_sm):
        print("Масса: {} т".format(self.width * self.length * weight_of_one_sm * amount_of_sm / 1000))

    def __init__(self, length, width):
        self.length = length
        self.width = width


road = Road(20, 5000)
road.calc_mass(25, 5)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
#    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    _Income = {"wage": 0, "bonus": 0}
    name = ""
    surname = ""
    position = ""
    income = _Income


class Position(Worker):
    def get_full_name(self):
        return "Full name: {}".format(self.name + " " + self.surname)

    def get_total_income(self):
        return "Total income: {}".format(self.income.get("wage") + self.income.get("bonus"))


pos1 = Position()
pos1.income = {"wage": 100000, "bonus": 200000}
pos1.name = "Vasya"
pos1.surname = "Pupkin"
pos1.position = "developer"

print(pos1.get_full_name())
print(pos1.get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    speed: 0
    color: ""
    name: ""
    is_police: False

    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print("машина повернула на {}".format(direction))

    def show_speed(self):
        print("текущая скорость: {}".format(self.speed))

    def show_all_car_info(self):
        print("Машина '{}' с цветом {} и {}".format(self.name, self.color, "полицейская" if self.is_police is True else "не полицейская"))
        return self


class TownCar(Car):
    def show_speed(self):
        print("текущая скорость: {} {}".format(self.speed, "" if self.speed < 60 else " - превышении скорости"))
        return self


class WorkCar(Car):
    def show_speed(self):
        print("текущая скорость: {} {}".format(self.speed, "" if self.speed < 40 else " - превышении скорости"))


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


TownCar(70, "красный", "honda civic", False).show_all_car_info().show_speed()
WorkCar(30, "оранжевый", "камаз", False).show_all_car_info().show_speed()
SportCar(130, "красный", "ford mustang", False).show_all_car_info().show_speed()
PoliceCar(20, "синий", "ваз 2109", True).show_all_car_info().show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#    В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title: ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


Pen().draw()
Handle().draw()
Pencil().draw()