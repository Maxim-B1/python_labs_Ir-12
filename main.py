class Airplane:
    public_number = 0
    public_string = ''
    def __init__(self, name="Ан-225 «Мрія»",  volume=300000, passenger=0, ):
        self.__passenger = passenger
        self.__volume = volume
        self.__name = name

    def __str__(self):
        return f"Назва літака: {self.__name}\nОб'єм топливного баку: {self.__volume} літрів\nКількість пасажирів: {self.__passenger}"

    def __repr__(self):
        return f"Airplane({self.__name}, {self.__volume}, {self.__passenger})"

    def get_name(self):
        return self.__name

    def get_passenger(self):
        return self.__passenger

    def get_volume(self):
        return self.__volume

    def set_name(self, name):
        self.__name = name

    def set_passenger(self, passenger):
        self.__passenger = passenger

    def set_volume(self, volume):
        self.__volume = volume

    def __del__(self):
        print(f'Літак {self.__name} видалено')


def main():
    airplane1 = Airplane(name="Boeing 737-200", passenger=125, volume=15856)
    airplane2 = Airplane(name="Airbus A320-200", passenger=150, volume=24210)
    airplane3 = Airplane(name="McDonnell Douglas DC-9-10", passenger=90, volume=14300)
    airplane0 = Airplane()
    print(airplane1)
    print(airplane2)
    print(airplane3)
    print(airplane3.get_volume())
    print(airplane3.public_number)
    print(airplane0.public_number)




main()
print(Airplane())
