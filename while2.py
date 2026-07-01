while True:
    nilai = int(input("nilai kamu: "))

    if nilai <0 or nilai >100:
        print("nilai tidak valid")
        break

    if nilai >= 90:
        print("lulus predikat A")
    elif nilai >= 80:
        print("lulus predikat B")
    elif nilai >= 75:
        print("lulus predikat C")
    else:
        print("tidak lulus")