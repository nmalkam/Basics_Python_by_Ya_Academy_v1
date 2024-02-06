class Programmer:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.START_SALARY = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20,
        }
        self.salary = self.START_SALARY[position]
        self.work_time = 0
        self.earned = 0
        # if 'Junior' == position:
        #     self.salary = 10
        # elif 'Middle' == position:
        #     self.salary = 15
        # elif 'Senior' == position:
        #     self.salary = 20

    def work(self, time):
        self.work_time += time
        self.earned += self.salary * time
        # self.earned += self.salary[self.position] * time

    def rise(self):
        if 20 > self.salary:
            self.salary += 5
        else:
            self.salary += 1
        # if 'Junior' == self.position:
        #     self.position = 'Middle'
        # elif 'Middle' == self.position:
        #     self.position = 'Senior'
        # elif 'Senior' == self.position:
        #     self.salary['Senior'] = self.salary['Senior'] + 1

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
