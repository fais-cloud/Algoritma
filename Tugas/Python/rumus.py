import subprocess

satuanKecepatan = "km/jam"
satuanLuas = "cm²"
satuanVolume = "cm³"

def luas_persegi():
    print("=== Menghitung Luas Persegi ====\n")
    sisi = float(input("masukkan sisi (cm): "))
    luas = sisi**2
    luas = round(luas, 2)

    print("\n=> luas           :", luas, satuanLuas, "\n\n")

def luas_persegi_panjang():
    print("=== Menghitung Luas Persegi Panjang ===\n")
    panjang = float(input("masukkan panjang (cm): "))
    lebar = float(input("masukkan lebar   (cm): "))
    luas = panjang * lebar
    luas = round(luas, 2)

    print("\n=> luas              :", luas, satuanLuas, "\n\n")

def luas_segitiga():
    print("=== Menghitung Luas Segitiga ===\n")
    alas = float(input("masukkan alas   (cm): "))
    tinggi = float(input("masukkan tinggi (cm): "))
    luas = (1 / 2) * alas * tinggi
    luas = round(luas, 2)

    print("\n=> luas segitiga    :", luas, satuanLuas, "\n\n")

def volume_kubus():
    print("=== Menghitung Volume Kubus ===\n")
    sisi = float(input("masukkan sisi (cm): "))
    volume = sisi**3
    volume = round(volume, 2)

    print("\n=> volume         :", volume, satuanVolume, "\n\n")

def volume_balok():
    print("=== Volume Balok ===\n")
    panjang = float(input("masukkan panjang (cm): "))
    lebar = float(input("masukkan lebar   (cm): "))
    tinggi = float(input("masukkan tinggi  (cm): "))
    volume = panjang * lebar * tinggi
    volume = round(volume, 2)

    print("\n=> volume balok      :", volume, satuanVolume, "\n\n")

def volume_bola():
    print("=== Volume Bola ===\n")
    r = float(input("masukkan jari-jari (cm): "))
    volume =  (4 / 3) * 3.14 * (r**3)
    volume = round(volume, 2)
    print("\n=> volume bola         :", volume, satuanVolume, "\n\n")

def hitung_kecepatan():
    print("=== Menghitung Kecepatan ===\n")
    jarak = float(input("masukkan jarak    (km): "))
    waktumenit = float(input("masukkan waktu (menit): "))
    waktu = waktumenit / 60
    kecepatan = jarak / waktu

    print("\n=> kecepatan          :", int(kecepatan), satuanKecepatan, "\n")

def hitung_waktu():
    print("=== Menghitung Waktu ===\n")
    jarak = float(input("masukkan jarak         (km): "))
    kecepatan = float(input("masukkan kecepatan (km/jam): "))
    waktu = (jarak / kecepatan) * 60
   
    print("\n=> waktu                   :", int(waktu), "menit\n")

def hitung_jarak():
    print("=== Menghitung Jarak ===\n")
    kecepatan = float(input("masukkan kecepatan (km/jam): "))
    waktu = float(input("masukkan waktu      (menit): "))
    jarak = kecepatan * (waktu / 60)
    jarak = round(jarak, 2)

    print("\n=> jarak                   :", (jarak), "km\n")

while True:
    print("\nPilih Kategori Rumus:")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    print("3. Kecepatan")
    print("0. Keluar")

    kategori = int(input("\npilih nomor kategori: "))
    subprocess.run(["cls"], shell=True)
    if kategori == 1:
        while True:
            print("=== Daftar Bangun Datar ===")
            print("1. luas persegi")
            print("2. luas persegi panjang")
            print("3. luas segitiga")
            print("0. kembali")

            userInput = int(input("\npilih rumus yang ingin dipakai: "))
            subprocess.run(["cls"], shell=True)
            if userInput == 1:
                luas_persegi()
            elif userInput == 2:
                luas_persegi_panjang()
            elif userInput == 3:
                luas_segitiga()
            else:
                break

    elif kategori == 2:
        while True:
            print("=== Daftar Bangun Ruang ===")
            print("1. kubus")
            print("2. volume balok")
            print("3. volume bola")
            print("0. kembali")

            userInput = int(input("\npilih rumus yang ingin dipakai: "))
            subprocess.run(["cls"], shell=True)
            if userInput == 1:
                volume_kubus()
            elif userInput == 2:
                volume_balok()
            elif userInput == 3:
                volume_bola()
            else:
                break

    elif kategori == 3:
        while True:
            print("=== Rumus Kecepatan ===")
            print("1. cari kecepatan")
            print("2. cari waktu")
            print("3. cari jarak")
            print("0. kembali")
        
            userInput = int(input("\npilih rumus yang ingin dipakai: "))
            subprocess.run(["cls"], shell=True)
            if userInput == 1:
                hitung_kecepatan()
            elif userInput == 2:
                hitung_waktu()
            elif userInput == 3:
                hitung_jarak()
            else:
                break
                
    else:
        break