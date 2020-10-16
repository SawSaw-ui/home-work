class Statyonary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки\n{self.title}'


class Pen(Statyonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки ручкой'


class Pencil(Statyonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки карандашом'


class Handle(Statyonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки маркером'


s = Statyonary('Выбор инструмента')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(s.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
