my_dict = {
    'tuple': (1, 2, '3', 4, 5),
    'list': [1, 'two', 3, 'Four', 5],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {1, '2', 3, 4, 5}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('Six')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = True
my_dict['dict'].pop('three')

my_dict['set'].add(8)
my_dict['set'].remove('2')

print(my_dict)
