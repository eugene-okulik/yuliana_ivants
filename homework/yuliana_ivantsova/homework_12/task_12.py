from flowers import Rose, Tulip, Lily
from bouquet import Bouquet

rose = Rose('red', 10, 20, 200)
tulip = Tulip('blue', 45, 50, 30)
lily = Lily('blue', 10, 90, 100)
bouquet = Bouquet(rose, tulip, lily)

print(bouquet.flowers_list)
print(
    f"Среднее время увядания: "
    f"{bouquet.get_average_wilting_time_bouguet()} дней"
)
print(f"Общая стоимость: {bouquet.get_total_price()} руб.")

print("Красные цветы:", bouquet.search_by(color='red'))
print("Цена 100 руб:", bouquet.search_by(price=100))
print("Свежесть 90%:", bouquet.search_by(freshness=90))
print("Длина стебля 45 см:", bouquet.search_by(stem_length=45))
print("Красные и цена 200:", bouquet.search_by(color='red', price=200))
