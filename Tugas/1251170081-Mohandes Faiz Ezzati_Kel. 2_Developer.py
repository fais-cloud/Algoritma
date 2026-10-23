"""Analisis Ω, O, Θ: mencari 1 KTM di 300 dompet"""

# KELOMPOK 2 :
# 1. Raihan Ahmad Priyono (1251170025): Project Manajer
# 2. Fakhrul Rozi Armadani (1251170152): System Analyst
# 3. Mohandes Faiz Ezzati Humaedi (1251170081): Programmer

# ---------- 1. PARAMETER ----------
N = 300                                  # jumlah dompet
WAKTU_PERTAMA = 3                        # detik, dompet ke-1
WAKTU_TOTAL = 180                        # detik, sampai dompet ke-300
WAKTU_LAIN = (WAKTU_TOTAL - WAKTU_PERTAMA) / (N - 1)   # detik/dompet ke-2..300

# ---------- 2. ALGORITMA ----------
def cari_ktm(tumpukan_dompet, target, tampil=False):
    """Mengembalikan (jumlah_iterasi, total_waktu)."""
    waktu = 0
    for i, dompet in enumerate(tumpukan_dompet, start=1):   # i = nomor iterasi
        waktu += WAKTU_PERTAMA if i == 1 else WAKTU_LAIN
        if tampil and (i <= 3 or i % 100 == 0 or dompet == target):
            print(f"  iterasi {i:>3} | {dompet:<9} | kumulatif {waktu:>6.1f} detik")
        if dompet == target:                                # KTM ketemu
            return i, waktu
    return N, waktu                                         # tidak ada

def tumpukan(posisi):
    dompet = [f"orang_{i}" for i in range(1, N + 1)]
    dompet[posisi - 1] = "KTM"
    return dompet

# ---------- 3. BEST CASE & WORST CASE ----------
print("BEST-CASE (KTM di dompet ke-1)")
best = cari_ktm(tumpukan(1), "KTM", tampil=True)

print("\nWORST-CASE (KTM di dompet ke-300)")
worst = cari_ktm(tumpukan(N), "KTM", tampil=True)

# ---------- 4. RATA-RATA: KTM di posisi 1..N, peluang sama ----------
semua = [cari_ktm(tumpukan(p), "KTM") for p in range(1, N + 1)]
rata_i = sum(i for i, _ in semua) / N                       # = (N+1)/2
rata_w = sum(w for _, w in semua) / N

# ---------- 5. RINGKASAN ----------
print("\nRINGKASAN")
print(f"Best-Case  : {best[0]:>5} iterasi | {best[1]:>6.1f} detik -> Ω(1)")
print(f"Worst-Case : {worst[0]:>5} iterasi | {worst[1]:>6.1f} detik -> O(N)")
print(f"Rata-rata  : {rata_i:>5.1f} iterasi | {rata_w:>6.1f} detik -> Θ(N)")

# ---------- 6. VERIFIKASI Θ(N): c1·n <= f(n) <= c2·n ----------
c1, c2 = 0.5, 1.0
print(f"Θ(N) terpenuhi: {c1}·{N} <= {rata_i:.1f} <= {c2}·{N} -> {c1 * N <= rata_i <= c2 * N}")