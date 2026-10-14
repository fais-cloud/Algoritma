"""
Analisis Asimtotik: Mencari 1 KTM di antara N dompet yang berserakan
Algoritma : Linear Search (Pencarian Linier)
Notasi    : Omega (best), O (worst), Theta (average)

Model waktu (diturunkan dari data kasus):
  - Dompet ke-1 memakan waktu 3 detik (termasuk waktu "pemanasan": mengambil & membuka dompet pertama)
  - Total seluruh 300 dompet = 300 detik
  - Maka 299 dompet sisanya berbagi 297 detik  ->  297/299 ~ 0,9933 detik/dompet
"""

import random
from dataclasses import dataclass

# ---------------------------------------------------------------
# 1. PARAMETER KASUS
# ---------------------------------------------------------------
N = 300                      # jumlah dompet
WAKTU_DOMPET_PERTAMA = 3.0   # detik
WAKTU_TOTAL = 300.0          # detik (seluruh dompet diperiksa)
WAKTU_PER_DOMPET_LAIN = (WAKTU_TOTAL - WAKTU_DOMPET_PERTAMA) / (N - 1)


def waktu_kumulatif(k: int) -> float:
    """Waktu (detik) untuk memeriksa dompet ke-1 s.d. ke-k."""
    if k <= 0:
        return 0.0
    return WAKTU_DOMPET_PERTAMA + (k - 1) * WAKTU_PER_DOMPET_LAIN


# ---------------------------------------------------------------
# 2. ALGORITMA (Linear Search) + PENGHITUNG LANGKAH f(n)
# ---------------------------------------------------------------
@dataclass
class Dompet:
    nama: str


def cari_ktm(tumpukan_dompet, target):
    """Mengembalikan (hasil, jumlah_langkah)."""
    langkah = 0
    for dompet in tumpukan_dompet:
        langkah += 1                      # 1 dompet diperiksa = 1 langkah dasar
        if dompet.nama == target:
            return "Ketemu!", langkah
    return "Tidak Ada", langkah


def buat_tumpukan(n, posisi_ktm):
    """Buat n dompet; KTM ada di posisi_ke-... (1-indexed). None = tidak ada."""
    tumpukan = [Dompet(f"orang_{i}") for i in range(1, n + 1)]
    if posisi_ktm is not None:
        tumpukan[posisi_ktm - 1] = Dompet("KTM_TARGET")
    return tumpukan


# ---------------------------------------------------------------
# 3. ANALISIS KASUS
# ---------------------------------------------------------------
def analisis_kasus(nama, posisi):
    tumpukan = buat_tumpukan(N, posisi)
    hasil, langkah = cari_ktm(tumpukan, "KTM_TARGET")
    waktu = waktu_kumulatif(langkah)
    print(f"{nama:<28}| posisi KTM: {str(posisi):>4} | langkah: {langkah:>3} "
          f"| waktu: {waktu:>7.2f} detik | {hasil}")
    return langkah, waktu


print("=" * 90)
print(f"ANALISIS PENCARIAN KTM  (N = {N} dompet)")
print("=" * 90)
print(f"Waktu dompet ke-1       : {WAKTU_DOMPET_PERTAMA:.2f} detik")
print(f"Waktu dompet ke-2..{N}  : {WAKTU_PER_DOMPET_LAIN:.4f} detik/dompet")
print("-" * 90)

# Best case  -> KTM di dompet pertama
langkah_best, waktu_best = analisis_kasus("Best-Case  (dompet pertama)", 1)
# Worst case -> KTM di dompet terakhir (atau tidak ada)
langkah_worst, waktu_worst = analisis_kasus("Worst-Case (dompet terakhir)", N)
analisis_kasus("Worst-Case (KTM tidak ada)", None)

# Average case -> KTM bisa berada di posisi mana saja dengan peluang sama (1/N)
semua_waktu = []
semua_langkah = []
for pos in range(1, N + 1):
    _, langkah = cari_ktm(buat_tumpukan(N, pos), "KTM_TARGET")
    semua_langkah.append(langkah)
    semua_waktu.append(waktu_kumulatif(langkah))

rata_langkah = sum(semua_langkah) / N
rata_waktu = sum(semua_waktu) / N
print("-" * 90)
print(f"{'Average-Case (semua posisi)':<28}| langkah rata-rata: {rata_langkah:.1f} "
      f"(= (N+1)/2) | waktu rata-rata: {rata_waktu:.2f} detik")

# ---------------------------------------------------------------
# 4. KESIMPULAN NOTASI ASIMTOTIK
# ---------------------------------------------------------------
print("\n" + "=" * 90)
print("KESIMPULAN NOTASI ASIMTOTIK")
print("=" * 90)
print(f"Kasus Terbaik  (Best-Case)  : f(n) = 1 langkah  ({waktu_best:.0f} detik)  -> Omega(1)")
print(f"Kasus Terburuk (Worst-Case) : f(n) = N langkah  ({waktu_worst:.0f} detik) -> O(N)")
print(f"Laju Pertumbuhan Rata-rata  : f(n) = (N+1)/2    ({rata_waktu:.1f} detik) -> Theta(N)")

# ---------------------------------------------------------------
# 5. VERIFIKASI FORMAL Theta(N):  c1*g(n) <= f(n) <= c2*g(n),  g(n) = n
#    f(n) = rata-rata langkah = (n+1)/2
# ---------------------------------------------------------------
print("\n" + "=" * 90)
print("VERIFIKASI FORMAL  c1.g(n) <= f(n) <= c2.g(n)   untuk semua n >= n0")
print("=" * 90)
c1, c2, n0 = 0.5, 1.0, 1
print(f"Dipilih: c1 = {c1}, c2 = {c2}, n0 = {n0}, g(n) = n\n")
print(f"{'n':>8} | {'c1*g(n)':>10} | {'f(n)=(n+1)/2':>13} | {'c2*g(n)':>10} | terpenuhi?")
valid = True
for n in (1, 10, 100, 300, 1_000, 10_000, 100_000):
    f_n = (n + 1) / 2
    ok = c1 * n <= f_n <= c2 * n
    valid &= ok
    print(f"{n:>8} | {c1*n:>10.1f} | {f_n:>13.1f} | {c2*n:>10.1f} | {ok}")
print(f"\nSemua titik uji terpenuhi -> f(n) = Theta(N): {valid}")

# ---------------------------------------------------------------
# 6. SIMULASI PERTUMBUHAN: acak posisi KTM untuk berbagai ukuran N
# ---------------------------------------------------------------
print("\n" + "=" * 90)
print("SIMULASI MONTE CARLO (1.000 percobaan per ukuran N): rasio langkah/N")
print("=" * 90)
random.seed(42)
print(f"{'N':>8} | {'rata-rata langkah':>18} | {'rasio langkah/N':>16}")
for n in (10, 100, 300, 1_000, 5_000):
    total = 0
    for _ in range(1_000):
        posisi = random.randint(1, n)
        total += posisi            # linear search butuh 'posisi' langkah
    rata = total / 1_000
    print(f"{n:>8} | {rata:>18.1f} | {rata / n:>16.3f}")
print("\nRasio konstan (~0,5) saat N membesar => pertumbuhan linier => Theta(N).")
