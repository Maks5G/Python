leng = int(input("Уведіть довжину хвилі в нм: "))
if leng < 380 or leng > 750:
    print("Не в діапазоні")
elif leng < 450:
    print("Хвиля в фіолетовому діапазоні")
elif leng < 495:
    print("Хвиля в синьому діапазоні")
elif leng < 570:
    print("Хвиля в зеленому діапазоні")
elif leng < 590:
    print("Хвиля в жовтому діапазоні")
elif leng < 620:
    print("Хвиля в помаранчевому діапазоні")
elif leng <= 750:
    print("Хвиля в червоному діапазоні")