class Programmer:
    __rank = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.salary = 0
        self.work_time = 0
        self.earned = 0
        self.bonus = 0

    def work(self, time):
        self.work_time += time
        self.earned += (self.__rank[self.position] + self.bonus) * time

    def rise(self):
        # if 20 != self.salary:
        #     self.salary += 5
        # else:
        #     self.salary += 1
        match self.position:
            case 'Junior':
                self.position = 'Middle'
            case 'Middle':
                self.position = 'Senior'
            case 'Senior':
                self.bonus += 1

    def info(self):
        # print(self.salary[self.position])
        return f'{self.name} {self.work_time}ч. {self.earned}тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

programmer1 = Programmer('Вас н', 'Senior')
programmer1.work(750)
print(programmer1.info())
programmer1.rise()
programmer1.work(500)
print(programmer1.info())
programmer1.rise()
programmer1.work(250)
print(programmer1.info())
programmer1.rise()
programmer1.work(250)
print(programmer1.info())

programmer.work(250)
print(programmer.info())
