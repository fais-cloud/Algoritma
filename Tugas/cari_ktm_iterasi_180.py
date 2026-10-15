"""
Analisis Asimtotik dengan PENELUSURAN ITERASI
Kasus: mencari 1 KTM di antara 300 dompet (Linear Search)

Ubah TAMPILKAN_SEMUA = True untuk mencetak seluruh 300 iterasi.
"""

# ------------------------------------------------------------
# 1. PARAMETER KASUS
# ------------------------------------------------------------
N = 300
WAKTU_PERTAMA = 3                                        # detik, dompet ke-1
WAKTU_TOTAL = 180                                        # detik, sampai dompet ke-300
WAKTU_LAIN = (WAKTU_TOTAL - WAKTU_PERTAMA) / (N - 1)     # detik/dompet ke-2..N
TAMPILKAN_SEMUA = False                                  # True = cetak semua iterasi


def waktu_dompet(k):
    """Waktu (detik) untuk memeriksa dompet ke-k saja."""
    return WAKTU_PERTAMA if k == 1 else WAKTU_LAIN


def buat_tumpukan(posisi_ktm=None):
    dompet = [f"orang_{i}" for i in range(1, N + 1)]
    if posisi_ktm:
        dompet[posisi_ktm - 1] = "KTM"
    return dompet


# ------------------------------------------------------------
# 2. ALGORITMA DENGAN TRACE ITERASI
# ------------------------------------------------------------
def cari_ktm(tumpukan_dompet, target, trace=False):
    """Mengembalikan (hasil, jumlah_iterasi, total_waktu)."""
    iterasi = 0
    total_waktu = 0.0

    if trace:
        print(f"{'Iterasi':>7} | {'Isi dompet':<10} | {'Waktu':>7} | {'Kumulatif':>10} | Cocok?")
        print("-" * 56)

    for dompet in tumpukan_dompet:          # <- setiap putaran = 1 iterasi = 1 langkah
        iterasi += 1
        total_waktu += waktu_dompet(iterasi)
        cocok = dompet == target

        # Cetak: 5 iterasi awal, tiap kelipatan 50, 2 iterasi terakhir, atau saat ketemu
        if trace and (TAMPILKAN_SEMUA or iterasi <= 5 or iterasi % 50 == 0
                      or iterasi >= N - 1 or cocok):
            print(f"{iterasi:>7} | {dompet:<10} | {waktu_dompet(iterasi):>6.2f}s "
                  f"| {total_waktu:>9.2f}s | {'YA -> Ketemu!' if cocok else 'tidak'}")

        if cocok:
            return "Ketemu!", iterasi, total_waktu

    return "Tidak Ada", iterasi, total_waktu


# ------------------------------------------------------------
# 3. TRACE TIAP KASUS
# ------------------------------------------------------------
print("=" * 70)
print(f"BEST-CASE: KTM ada di dompet pertama  (N = {N})")
print("=" * 70)
hasil, best_iter, best_waktu = cari_ktm(buat_tumpukan(1), "KTM", trace=True)
print(f"=> {hasil} | {best_iter} iterasi | {best_waktu:.1f} detik  ->  Ω(1)\n")

print("=" * 70)
print(f"WORST-CASE: KTM ada di dompet terakhir (ke-{N})")
print("=" * 70)
hasil, worst_iter, worst_waktu = cari_ktm(buat_tumpukan(N), "KTM", trace=True)
print(f"=> {hasil} | {worst_iter} iterasi | {worst_waktu:.1f} detik  ->  O(N)\n")

print("=" * 70)
print("RATA-RATA: KTM di dompet ke-150 (posisi tengah) sebagai contoh")
print("=" * 70)
hasil, tengah_iter, tengah_waktu = cari_ktm(buat_tumpukan(150), "KTM", trace=True)
print(f"=> {hasil} | {tengah_iter} iterasi | {tengah_waktu:.1f} detik\n")

# ------------------------------------------------------------
# 4. RATA-RATA SEBENARNYA: jalankan pencarian untuk SEMUA posisi (1..N)
# ------------------------------------------------------------
total_iter, total_waktu_all = 0, 0.0
for posisi in range(1, N + 1):
    _, it, w = cari_ktm(buat_tumpukan(posisi), "KTM")
    total_iter += it
    total_waktu_all += w

rata_iter = total_iter / N
rata_waktu = total_waktu_all / N

print("=" * 70)
print(f"RATA-RATA dari {N} skenario (KTM di posisi 1 s.d. {N}, peluang sama)")
print("=" * 70)
print(f"Total iterasi seluruh skenario : {total_iter}")
print(f"Rata-rata iterasi              : {rata_iter:.1f}  (= (N+1)/2)")
print(f"Rata-rata waktu                : {rata_waktu:.1f} detik\n")

# ------------------------------------------------------------
# 5. RINGKASAN
# ------------------------------------------------------------
print("=" * 70)
print("RINGKASAN")
print("=" * 70)
print(f"{'Kasus':<22}| {'Iterasi':>8} | {'Waktu (detik)':>13} | Notasi")
print("-" * 62)
print(f"{'Best-Case':<22}| {best_iter:>8} | {best_waktu:>13.1f} | Ω(1)")
print(f"{'Worst-Case':<22}| {worst_iter:>8} | {worst_waktu:>13.1f} | O(N)")
print(f"{'Rata-rata':<22}| {rata_iter:>8.1f} | {rata_waktu:>13.1f} | Θ(N)")

# Verifikasi Θ(N): c1·n <= f(n) <= c2·n, dengan f(n) = rata-rata iterasi
c1, c2 = 0.5, 1.0
print(f"\nVerifikasi Θ(N): {c1}·{N} <= {rata_iter:.1f} <= {c2}·{N}  ->  "
      f"{c1 * N <= rata_iter <= c2 * N}")
