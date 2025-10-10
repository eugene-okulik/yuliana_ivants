from datetime import datetime, timedelta


class Flowers:

    def __init__(self, name, color, stem_length, freshness, price, lifespan_days):
        self.__name = name
        self.__price = price
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.lifespan_days = lifespan_days
        self.created_date = datetime.now()


    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} ({self.color}) - {self.price} руб."

    def __repr__(self):
        return f"{self.__name} ({self.color}) - {self.price} руб."

    @price.setter
    def price(self, value):
        self.__price = value

    def get_wilting_date(self):
        return self.created_date + timedelta(days=self.lifespan_days)



class Rose(Flowers):
    __name = 'Rose'
    def __init__(self, color, stem_length, freshness, price, lifespan_days):
        super().__init__(self.__name, color, stem_length, freshness, price, lifespan_days)

class Lily(Flowers):
    __name = 'Lily'
    def __init__(self, color, stem_length, freshness, price, lifespan_days):
        super().__init__(self.__name, color, stem_length, freshness, price, lifespan_days)

class Tulip(Flowers):
    __name = 'Tulip'
    def __init__(self, color, stem_length, freshness, price, lifespan_days):
        super().__init__(self.__name, color, stem_length, freshness, price, lifespan_days)


class Bouquet:
    def __init__(self, *args):
        self.flowers_list = list(args)



rose = Rose('red', '10', '20', '30', 4)
tulip = Tulip('blue', '10', '20', '30', 3)
lily = Lily('blue', '10', '20', '30', 3)
bouquet = Bouquet(rose, tulip, lily)
print(bouquet.flowers_list)
