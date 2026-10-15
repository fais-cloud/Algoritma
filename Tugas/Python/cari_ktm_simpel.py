N = 300                                  # jumlah dompet
WAKTU_PERTAMA = 3                        # detik, dompet pertama
WAKTU_LAIN = (300 - 3) / (N - 1)         # detik/dompet sisanya (total 300 detik)


def cari_ktm(tumpukan_dompet, target):
    langkah = 0
    for dompet in tumpukan_dompet:
        langkah += 1
        if dompet == target:
            return "Ketemu!", langkah
    return "Tidak Ada", langkah


def waktu(langkah):
    return WAKTU_PERTAMA + (langkah - 1) * WAKTU_LAIN


def tumpukan(posisi):
    dompet = [f"orang_{i}" for i in range(1, N + 1)]
    if posisi:
        dompet[posisi - 1] = "KTM"
    return dompet


# Best case: KTM di dompet pertama
_, best = cari_ktm(tumpukan(1), "KTM")

# Worst case: KTM di dompet terakhir
_, worst = cari_ktm(tumpukan(N), "KTM")

# Rata-rata: KTM bisa di posisi mana saja (peluang sama)
langkah_semua = [cari_ktm(tumpukan(p), "KTM")[1] for p in range(1, N + 1)]
rata = sum(langkah_semua) / N

print(f"Best-Case  : {best:>3} langkah | {waktu(best):>6.1f} detik -> Ω(1)")
print(f"Worst-Case : {worst:>3} langkah | {waktu(worst):>6.1f} detik -> O(N)")
print(f"Rata-rata  : {rata:>5.1f} langkah | {sum(map(waktu, langkah_semua))/N:>6.1f} detik -> Θ(N)")
