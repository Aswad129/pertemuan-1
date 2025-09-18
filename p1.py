# Program Peminjaman Buku Perpustakaan

anggota = input("Apakah Citra anggota perpustakaan? (ya/tidak): ")

if anggota.lower() == "ya":
    print("Citra boleh meminjam buku.")
    print("Mencetak daftar peminjaman untuk 5 buku:\n")
    
    # perulangan untuk cetak 5 daftar buku
    for i in range(1, 6):
        print(f"Daftar peminjaman buku ke-{i} dicetak")
else:
    print("Citra tidak boleh meminjam buku karena bukan anggota.")




#Citra pergi ke perpustakaan sekolah karena ingin meminjam buku. Namun, di perpustakaan ada aturan khusus: hanya anggota perpustakaan yang diperbolehkan meminjam buku, sedangkan yang bukan anggota tidak boleh. Jika Citra terdaftar sebagai anggota, maka ia dapat langsung meminjam 5 buku sekaligus, dan sistem perpustakaan akan mencetak daftar peminjaman sebanyak 5 kali sesuai jumlah buku yang dipinjam. Buatlah program Python berdasarkan cerita tersebut untuk menentukan apakah Citra boleh meminjam buku dan menampilkan daftar peminjamannya.