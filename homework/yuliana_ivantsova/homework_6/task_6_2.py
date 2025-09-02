for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = 'FuzzBuzz'
    elif num % 5 == 0:
        num = 'buzz'
    elif num % 3 == 0:
        num = 'fuzz'
    print(num)
