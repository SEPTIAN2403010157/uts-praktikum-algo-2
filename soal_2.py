detik = int(input("Masukkan waktu dalam detik: "))
jam = detik // 3600  # 1 jam = 3600 detik
detik_sisa = detik % 3600
menit = detik_sisa // 60  # 1 menit = 60 detik
detik_akhir = detik_sisa % 60  # sisa detik
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik_akhir} detik")
