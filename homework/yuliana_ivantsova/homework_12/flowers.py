from datetime import datetime, timedelta


class Flowers:

    def __init__(
            self, name, color, stem_length, freshness, price, lifespan_days
    ):
        self.__name = name
        self.__price = price
        self.__lifespan_days = lifespan_days
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.created_date = datetime.now()

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def lifespan_days(self):
        return self.__lifespan_days

    def __str__(self):
        return f"{self.__name} ({self.color}) - {self.price} руб."

    def __repr__(self):
        return f"{self.__name} ({self.color}) - {self.price} руб."

    @price.setter
    def price(self, value):
        self.__price = value

    def get_wilting_date(self):
        return self.created_date + timedelta(days=self.__lifespan_days)

    def get_remaining_lifespan(self):
        return self.__lifespan_days


class Rose(Flowers):
    __name = 'Rose'
    __lifespan_days = 7

    def __init__(self, color, stem_length, freshness, price):
        super().__init__(
            self.__name, color, stem_length,
            freshness, price, self.__lifespan_days
        )


class Lily(Flowers):
    __name = 'Lily'
    __lifespan_days = 10

    def __init__(self, color, stem_length, freshness, price):
        super().__init__(
            self.__name, color, stem_length,
            freshness, price, self.__lifespan_days
        )


class Tulip(Flowers):
    __name = 'Tulip'
    __lifespan_days = 10

    def __init__(self, color, stem_length, freshness, price):
        super().__init__(
            self.__name, color, stem_length,
            freshness, price, self.__lifespan_days
        )
