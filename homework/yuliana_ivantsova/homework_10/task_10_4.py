PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split('\n')

price_dict = {
    items.split()[0]: int(items.split()[1].strip('р')) for items in price_list
}
print(price_dict)
