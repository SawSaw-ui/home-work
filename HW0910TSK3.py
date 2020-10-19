class Worker:
    def __init__(self, name, surname, position, wage, bonus, currency):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        self.currency = currency


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus, currency):
        super().__init__(name, surname, position, wage, bonus, currency)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

    def get_currency(self):
        return self.currency


x = Position('Alex', 'Smile', 'Engineer', 250, 500, 'EUR')
print(x.get_full_name())
print(x.position)
print(x.get_total_income())
print(x.get_currency())
