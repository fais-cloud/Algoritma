# SIMULASI PENCARIAN KTM PADA 300 DOMPET

# ==== DATA AWAL ====
jumlah_dompet = 300 # total dompet
waktu_dompet_pertama = 3 # detik untuk dompet_pertama
waktu_sistem = 180 # detik total (3 menit)
posisi_ktm = 300 # KTM ada di dompet ke-250

# ==== PERHITUNGAN DASAR ====
waktu_normal = jumlah_dompet 
waktu_dompet_pertama # 900 detik
waktu_rata_rata = waktu_sistem / jumlah_dompet # 0.6 detik per dompet

kecepatan_awal = 1 /waktu_dompet_pertama #0.33 dompet/detik
kecepatan_akhir = jumlah_dompet / waktu_sistem # 1.67 dompet/detik
percepatan = (kecepatan_akhir - kecepatan_awal) / waktu_sistem

garis = '=' *55 + '\n'

# ==== HEADER ====
print(garis, end='')
print("SIMULASI PENCARIAN KTM")
print(garis, end='')
print(f"Jumlah dompet: {jumlah_dompet}")
print(f"Waktu normal: {waktu_normal} detik")
print(f"Waktu sistem: {waktu_sistem} detik")
print(f"Rata-rata: {waktu_rata_rata:.2f} detik/dompet")
print(garis, end='')
print()

# ==== ITERASI ====
jumlah_pemeriksaan = 0
total_waktu = 0.0
kecepatan_terakhir = 0.0
percepatan_terakhir = 0.0
ditemukan = False

for i in range(1, jumlah_dompet + 1):
    jumlah_pemeriksaan += 1

    waktu =i * waktu_rata_rata # waktu kumulatif
    kecepatan = i / waktu # dompet/detik
    percepat = (kecepatan - kecepatan_awal) / waktu # dompet/detik^2

    total_waktu = waktu
    kecepatan_terakhir = kecepatan
    percepatan_terakhir = percepat

    print(f"iterasi {i}:")
    print(f" - Waktu: {waktu:.2f} detik")
    print(f" - Kecepatan: {kecepatan:.2f} dompet/detik")
    print(f" - Percepatan: {percepat:.4f} dompet/detik")

    if i == posisi_ktm:
        ditemukan = True
        print(" >> KTM ditemukan!")
        break

# ==== HASIL AKHIR ====
print('\n' + garis, end='')
print("HASIL AKHIR PENCARIAN")
print(garis, end='')
print(f"{posisi_ktm:<22}: {posisi_ktm if ditemukan else '-' }")
print(f"{'status':<22}: {'KTM ditemukan' if ditemukan else 'KTM tidak ditemukan'}")
print(f"{'Jumlah pemeriksaan':<22}: {jumlah_pemeriksaan}")
print(f"{'Total waktu':<22}: {total_waktu:.2f} detik")
print(f"{'Kecepatan awal':<22}: {kecepatan_awal:.2f} dompet/detik")
print(f"{'Kecepatan terakhir':<22}: {kecepatan_terakhir:.2f} dompet/detik")
print(f"{'Percepatan':<22}: {percepatan:.4f} dompet/detik")
print(garis, end='')
