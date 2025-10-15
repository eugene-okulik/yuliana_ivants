class Bouquet:

    def __init__(self, *args):
        self.flowers_list = list(args)

    def add_flower(self, flower):
        self.flowers_list.append(flower)

    def remove_flower(self, flower):
        self.flowers_list.remove(flower)

    def __len__(self):
        return len(self.flowers_list)

    def get_total_price(self):
        return sum(flower.price for flower in self.flowers_list)

    def get_average_wilting_time_bouguet(self):
        total_lifespan = sum(
            flower.get_remaining_lifespan() for flower in self.flowers_list
        )
        average_lifespan = total_lifespan / len(self.flowers_list)
        return average_lifespan

    def sort_by(self, key):
        return sorted(self.flowers_list, key=lambda x: getattr(x, key))

    def search_by(self, **filters):
        result = self.flowers_list

        for attr_name, value in filters.items():
            result = [
                flower for flower in result
                if getattr(flower, attr_name) == value
            ]

        return result
