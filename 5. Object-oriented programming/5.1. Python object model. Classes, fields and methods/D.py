class Programmer:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.work_time = 0
        self.earned = 0
        self.work_time_before_rise = 0
        if 'Junior' == position:
            self.salary = 10
        elif 'Middle' == position:
            self.salary = 15
        elif 'Senior' == position:
            self.salary = 20

    def work(self, time):
        self.work_time += time
        self.earned += self.salary * time
        # self.work_time - self.work_time_before_rise)
        # self.work_time_before_rise = self.work_time

    def rise(self):
        if 'Junior' == self.position:
            # self.earned += self.salary * self.work_time
            # self.work_time_before_rise = self.work_time
            self.position = 'Middle'
            self.salary = 15
        elif 'Middle' == self.position:
            # self.earned += self.salary * (self.work_time - self.work_time_before_rise)
            # self.work_time_before_rise = self.work_time
            self.position = 'Senior'
            self.salary = 20
        elif 'Senior' == self.position:
            # self.earned += self.salary * (self.work_time - self.work_time_before_rise)
            # self.work_time_before_rise = self.work_time
            self.salary += 1

    def info(self):
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
