class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина начала движение!'

    def stop(self):
        return 'Машина остановилась!'

    def turn(self, direction):
        return 'Машина повернула: ' + direction

    def show_speed(self):
        return f'Скорость: {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} Полицейская машина'
        else:
            return f'{self.name} Городска машина'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} составляет {self.speed}!')

        if self.speed > 60:
            return f'{self.name} привышает установленный лимит!'
        else:
            return f'{self.name} двигается с разрешенной скоростью!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} составляет {self.speed}!')

        if self.speed > 40:
            return f'{self.name} привышает установленный лимит!'
        else:
            return f'{self.name} двигается с разрешенной скоростью!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


maybach = TownCar(speed=75, color='Красный', name='Maybach', is_police=False)
print(maybach.name)
print(maybach.go())
print(maybach.turn('Налево!'))
print(maybach.stop())
print(maybach.show_speed())
print(maybach.police())
vaz = SportCar(speed=120, color='Черный, матовый!', name='ВАЗ 2109', is_police=False)
print(vaz.name)
print(vaz.go())
print(vaz.show_speed())
print(vaz.police())
print(vaz.turn('На право!'))
print(vaz.stop())
gaz66 = WorkCar(speed=50, color='Розовый, матовый!', name='ГАЗ 66', is_police=False)
print(gaz66.name)
print(gaz66.go())
print(gaz66.show_speed())
print(gaz66.police())
print(gaz66.turn('на ул.Строителей'))
print(gaz66.stop())
police = PoliceCar(speed=250, color='Жёлтый!', name='ГАЗ М1', is_police=True)
print(police.name)
print(police.go())
print(police.show_speed())
print(police.police())
print(police.turn('С улицы Строителей, в сторону частного сектора!!!'))
print(police.stop())

