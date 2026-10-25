<?php

$data = array();   // data mahasiswa
$undo = array();   // stack: NIM yang terakhir ditambahkan
$pesan = '';       // pesan singkat yang tampil di menu berikutnya

/* ---------- FUNGSI BANTU ---------- */
function bersihkan() {
    // aktifkan kode ANSI di Windows 10+ (PHP 7.2+)
    if (PHP_OS_FAMILY === 'Windows' && function_exists('sapi_windows_vt100_support')) {
        sapi_windows_vt100_support(STDOUT, true);
    }

    // pindah ke pojok kiri atas, hapus layar, lalu hapus riwayat scroll
    echo "\033[H\033[2J\033[3J";
}

function input($teks) {
    echo $teks;
    return trim(fgets(STDIN));
}

function jeda(){
    input("\nTekan Enter untuk lanjut...");
}

function tampilTabel($arr) {
    echo "No  NIM         Nama                 Nilai\n";
    echo "------------------------------------------\n";
    if (count($arr) == 0) {
        echo "(kosong)\n";
    }
    foreach ($arr as $i => $s) {
        echo str_pad($i + 1, 4) . str_pad($s['nim'], 12) . str_pad($s['nama'], 21) . $s['nilai'] . "\n";
    }
}

/* ---------- SORTING ---------- */
function bubbleSort($arr, $key) {
    $n = count($arr);
    for ($i = 0; $i < $n - 1; $i++) {
        for ($j = 0; $j < $n - $i - 1; $j++) {
            if ($arr[$j][$key] > $arr[$j + 1][$key]) {
                $t = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $t;
            }
        }
    }
    return $arr;
}

function selectionSort($arr, $key) {
    $n = count($arr);
    for ($i = 0; $i < $n - 1; $i++) {
        $min = $i;
        for ($j = $i + 1; $j < $n; $j++) {
            if ($arr[$j][$key] < $arr[$min][$key]) {
                $min = $j;
            }
        }
        $t = $arr[$i];
        $arr[$i] = $arr[$min];
        $arr[$min] = $t;
    }
    return $arr;
}

/* ---------- SEARCHING ---------- */
function linearSearch($arr, $nama) {
    foreach ($arr as $i => $s) {
        if (strcasecmp($s['nama'], $nama) == 0) {
            return $i;
        }
    }
    return -1;
}

function binarySearch($arr, $nim) {
    $low = 0;
    $high = count($arr) - 1;
    while ($low <= $high) {
        $mid = (int) (($low + $high) / 2);
        if ($arr[$mid]['nim'] == $nim) {
            return $mid;
        }
        if ($arr[$mid]['nim'] < $nim) {
            $low = $mid + 1;
        } else {
            $high = $mid - 1;
        }
    }
    return -1;
}

/* ---------- PROGRAM UTAMA ---------- */
while (true) {
    bersihkan();
    echo "=== Sistem Manajemen Nilai Mahasiswa ===\n\n";

    if ($pesan != '') {
        echo ">> $pesan\n\n";
        $pesan = '';
    }

    tampilTabel($data);

    echo "\n1. Tambah data\n";
    echo "2. Undo\n";
    echo "3. Urutkan nilai\n";
    echo "4. Cari nama\n";
    echo "5. Cari NIM\n";
    echo "6. Hapus data\n";
    echo "7. Reset\n";
    echo "0. Keluar\n";

    $pilih = input("\npilih menu: ");
    echo "\n";

    if ($pilih == '1') {
        $nim = input("NIM   : ");
        $nama = input("Nama  : ");
        $nilai = (int) input("Nilai : ");

        $data[] = array('nim' => $nim, 'nama' => $nama, 'nilai' => $nilai);  // langsung masuk
        $undo[] = $nim;                                                       // catat untuk undo
        $pesan = "Data $nama disimpan.";

    } elseif ($pilih == '2') {
        if (count($undo) > 0) {
            $nim = array_pop($undo);   // ambil dari atas stack
            foreach ($data as $i => $s) {
                if ($s['nim'] == $nim) {
                    unset($data[$i]);
                    break;
                }
            }
            $data = array_values($data);
            $pesan = 'Input terakhir dibatalkan.';
        } else {
            $pesan = 'Tidak ada yang bisa di-undo.';
        }

    } elseif ($pilih == '3') {
        $metode = input("Metode (1 = Bubble, 2 = Selection): ");
        echo "\n";

        $mulai = microtime(true);
        if ($metode == '2') {
            $hasil = selectionSort($data, 'nilai');
            $nama = 'Selection';
        } else {
            $hasil = bubbleSort($data, 'nilai');
            $nama = 'Bubble';
        }
        $ms = (microtime(true) - $mulai) * 1000;

        tampilTabel(array_reverse($hasil));  // nilai tertinggi di atas
        echo "\n$nama Sort : " . round($ms, 4) . " ms\n";
        jeda();

    } elseif ($pilih == '4') {
        $kunci = input("Nama yang dicari: ");
        $i = linearSearch($data, $kunci);
        if ($i >= 0) {
            echo "\nNama ditemukan di nomor " . ($i + 1) . "\n";
        } else {
            echo "\nNama tidak ditemukan.\n";
        }
        jeda();

    } elseif ($pilih == '5') {
        $kunci = input("NIM yang dicari: ");
        $urut = bubbleSort($data, 'nim');  // binary search butuh data terurut
        $i = binarySearch($urut, $kunci);
        if ($i >= 0) {
            echo "\n" . $urut[$i]['nama'] . " (nilai " . $urut[$i]['nilai'] . ")\n";
        } else {
            echo "\nNIM tidak ditemukan.\n";
        }
        jeda();

    } elseif ($pilih == '6') {
        $nim = input("NIM yang dihapus: ");
        $ketemu = false;
        foreach ($data as $i => $s) {
            if ($s['nim'] == $nim) {
                unset($data[$i]);
                $ketemu = true;
                break;
            }
        }
        $data = array_values($data);

        // hapus juga dari stack undo
        foreach ($undo as $k => $u) {
            if ($u == $nim) {
                unset($undo[$k]);
            }
        }
        $undo = array_values($undo);

        $pesan = $ketemu ? 'Data dihapus.' : 'Data tidak ditemukan.';

    } elseif ($pilih == '7') {
        $data = array();
        $undo = array();
        $pesan = 'Semua data direset.';

    } elseif ($pilih == '0') {
        break;
    }
}

echo "Program selesai.\n";

?>
