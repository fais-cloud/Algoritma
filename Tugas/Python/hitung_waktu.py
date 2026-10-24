import subprocess

def hitung_kecepatan():
    print("=== Menghitung Kecepatan ===\n")
    jarak = float(input("masukkan jarak (km): "))
    waktu = float(input("masukkan waktu (menit): "))
    kecepatan = jarak / (waktu / 60)

    print("\n=> kecepatan: ", int(kecepatan), "km/jam")

def hitung_waktu():
    print("=== Menghitung Waktu ===\n")
    jarak = float(input("masukkan jarak (km): "))
    kecepatan = float(input("masukkan kecepatan (km/jam): "))
    waktu = (jarak / kecepatan) * 60
   
    print("=> waktu: ", int(waktu), "menit")

def hitung_jarak():
    print("=== Menghitung Jarak ===\n")
    kecepatan = float(input("masukkan kecepatan (km/jam): "))
    waktu = float(input("masukkan waktu (menit): "))
    jarak = kecepatan * (waktu / 60)

    print("\n=> jarak: ", int(jarak), "km")

while True:
    userInput = input("\nPilih rumus yang akan dipakai: \n1. menghitung kecepatan\n2. menghitung Waktu\n3. menghitung jarak\n0. keluar\n\npilih nomor berapa: ")
    subprocess.run(["cls"], shell=True)
    if(userInput == "1"):
        hitung_kecepatan()
    elif(userInput == "2"):
        hitung_waktu()
    elif(userInput == "3"):
        hitung_jarak()
    else:
        break
