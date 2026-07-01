nilai = ""

while nilai != "q":
    nilai = input("nilai kamu (tekan q untuk keluar): ")

    if nilai != "q":
        nilai_angka = int(nilai)

        if nilai_angka < 0 or nilai_angka > 100:
            print("Nilai tidak valid")
        elif nilai_angka >= 90:
            print("Lulus predikat A")
        elif nilai_angka >= 80:
            print("Lulus predikat B")
        elif nilai_angka >= 75:
            print("Lulus predikat C")
        else:
            print("Tidak lulus")