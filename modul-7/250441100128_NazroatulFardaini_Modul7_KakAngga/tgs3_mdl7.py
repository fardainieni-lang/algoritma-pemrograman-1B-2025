kupon = {
    "DISC10": 10,
    "DISC20": 20,
    "HEMAT5": 5
}

keranjang = []


def menu_input():
    while True:
        try:
            return int(input("Pilih menu (1-4): "))
        except ValueError:
            print("Input harus angka!")


def tampilkan_kupon():
    print("=== KUPON YANG TERSEDIA ===")
    
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        for kode, diskon in kupon.items():
            print(f"{kode} -> Diskon {diskon}%")

    print()


def tambah_barang():
    print("=== Tambah Barang ===")
    nama = input("Nama barang: ")
    while True:
        try:
            harga = float(input("Harga barang: "))
            break
        except:
            print("Harga harus angka!")
    
    while True:
        try:
            jmlh_barang = int(input("Jumlah: "))
            break
        except:
            print("jumlah barang harus angka!")

    total = harga * jmlh_barang
    keranjang.append((nama, harga, jmlh_barang, total))
    print("Barang berhasil ditambahkan.")

def transaksi():
    print("=== PROSES TRANSAKSI ===")

    if not keranjang:
        print("Keranjang kosong! Tambah barang dulu.")
        return

    # Hitung total belanja
    total_belanja = sum(item[3] for item in keranjang)

    print("Daftar Belanja:")
    for brg, harga, jmlh_barang, total in keranjang:
        print(f"- {brg}, Harga: {harga}, jumlah barang: {jmlh_barang}, Total: {total}")

    print(f"Total belanja sebelum diskon: {total_belanja}")

    tampilkan_kupon()
    kode = input("Masukkan kode kupon (Enter jika tidak pakai): ").upper()

    if kode == "":
        print("Tidak menggunakan kupon.")
        total_akhir = total_belanja

    else:
        while kode not in kupon:
            print("Kupon telah dipakai atau tidak valid! Silahkan masukkan kupon lain.")
            tampilkan_kupon()
            kode = input("Masukkan kode kupon (Enter jika tidak pakai): ").upper()

            if kode == "":
                print("Tidak menggunakan kupon.")
                total_akhir = total_belanja
                break

        if kode != "":
            diskon = kupon[kode]
            total_akhir = total_belanja - (total_belanja * diskon / 100)
            print(f"Diskon {diskon}% diterapkan.")

            del kupon[kode]

    print(f"Total bayar: {total_akhir}")

    keranjang.clear()

while True:
    print("===== PROGRAM KUPON DISKON =====")
    print("1. Tampilkan Kupon")
    print("2. Tambah Barang")
    print("3. Transaksi")
    print("4. Keluar")

    pilih = menu_input()

    if pilih == 1:
        tampilkan_kupon()
    elif pilih == 2:
        tambah_barang()
    elif pilih == 3:
        transaksi()
    elif pilih == 4:
        print("Keluar")
        break
    else:
        print("Menu tidak tersedia.")