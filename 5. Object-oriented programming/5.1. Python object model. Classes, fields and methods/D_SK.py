class Programmer:
    __wage = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }
    print(__wage.keys())
    __ranks = list(dict(sorted(__wage.items(), key=lambda item: item[1])).keys())  # noqa
    print(__ranks)
    print()
    print(dict(sorted(__wage.items(), key=lambda item: item[1])).keys())  # noqa
    print()
    print(sorted(__wage.items(), key=lambda item: item[1]))
    print()
    print(__wage.items())


    def __init__(self, name, position) -> None:
        self.__name = name
        self.__position = position
        self.__bonus = 0
        self.__work_time = 0
        self.__salary = 0

    def work(self, time):
        self.__work_time += time
        self.__salary += (self.__wage[self.__position] + self.__bonus) * time

    def info(self):
        return f'{self.__name} {self.__work_time}ч. {self.__salary}тгр.'

    def rise(self):
        if self.__position != self.__ranks[-1]:
            index = self.__ranks.index(self.__position)
            self.__position = self.__ranks[index + 1]
        else:
            self.__bonus += 1


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
