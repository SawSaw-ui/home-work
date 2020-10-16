class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def allmass(self):
        self.weight = 25
        self.thickness = 0.5
        mass = self._lenght * self._width * self.thickness * self.weight / 1000
        print(f'Для постройки необходимо {mass} тонн асфальта!')

    def mass_m(self):
        self.weight = 25
        self.thickness = 0.1
        mass = self._lenght * self._width * self.thickness * self.weight / 1000
        print(f'Для постройки - 1м2 (проектная толщина 1 см) - необходимо {mass} кг., асфальта!')


rm = Road(1000, 20)
rm.allmass()
rm.mass_m()
