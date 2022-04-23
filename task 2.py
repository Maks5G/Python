equivalent = {('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'): 1,
              ('D', 'G'): 2,
              ('B', 'C', 'M', 'P'): 3,
              ('F', 'H', 'V', 'W', 'Y'): 4,
              'K': 5,
              ('J', 'X'): 8,
              ('Q', 'Z'): 10}

str = str.upper(input("Уведіть строку літер: "))
total = 0

for el in str:
    for key, value in equivalent.items():
        for el_key in key:
            if el == el_key:
                total += value
print("Кількість балів:", total)







