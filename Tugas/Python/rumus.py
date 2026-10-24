import subprocess

satuanKecepatan = "km/jam"
satuanLuas = "cm²"
satuanVolume = "cm³"

def hitung_kecepatan():
    print("=== Menghitung Kecepatan ===\n")
    jarak = float(input("masukkan jarak (km): "))
    waktumenit = float(input("masukkan waktu (menit): "))
    waktu = waktumenit / 60
    kecepatan = jarak / waktu

    print("\n=> kecepatan : ", int(kecepatan), satuanKecepatan)
    print("\ntekan enter untuk kembali")

def luas_persegi():
    print("=== Menghitung Luas Persegi ===\n")
    sisi = float(input("masukkan sisi (cm): "))
    luas = sisi**2

    print("\n=> luas : ", luas, satuanLuas)
    print("\ntekan enter untuk kembali")

def luas_persegi_panjang():
    print("=== Menghitung Luas Persegi Panjang ===\n")
    panjang = float(input("masukkan panjang (cm) :"))
    lebar = float(input("masukkan lebar (cm) :"))
    luas = panjang * lebar

    print("\n=> luas :", luas, satuanLuas)
    print("\ntekan enter untuk kembali")

def luas_segitiga():
    print("=== Menghitung Luas Segitiga ===\n")
    alas = float(input("masukkan alas (cm): "))
    tinggi = float(input("masukkan tinggi (cm): "))
    luas = (1 / 2) * alas * tinggi

    print("\n=> luas segitiga : ", luas, satuanLuas)
    print("\ntekan enter untuk kembali")

def volume_balok():
    print("=== Volume Balok ===\n")
    panjang = float(input("masukkan panjang (cm): "))
    lebar = float(input("masukkan lebar (cm): "))
    tinggi = float(input("masukkan tinggi (cm) "))
    volume = panjang * lebar * tinggi

    print("\n=> volume balok : ", volume, satuanVolume)
    print("\ntekan enter untuk kembali")

def volume_bola():
    print("=== Volume Bola ===\n")
    r = float(input("masukkan jari-jari (cm): "))
    volume =  (4 / 3) * 3.14 * (r**3)

    print("\n=> volume bola : ", volume, satuanVolume)
    print("\ntekan enter untuk kembali")

while True:
    userInput = int(input("\nPilih rumus yang ingin dipakai: \n1. kecepatan\n2. luas persegi\n3. luas persegi panjang\n4. luas segitiga\n5. volume balok\n6. volume bola\n0. keluar\n\npilih nomor berapa: "))
    subprocess.run(["cls"], shell=True)
    if(userInput == 1):
        hitung_kecepatan()
    elif(userInput == 2):
        luas_persegi()
    elif(userInput == 3):
        luas_persegi_panjang()
    elif(userInput == 4):
        luas_segitiga()
    elif(userInput == 5):
        volume_balok()
    elif(userInput == 6):
        volume_bola()
    else:
        break
