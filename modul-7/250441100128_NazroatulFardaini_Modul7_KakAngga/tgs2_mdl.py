inventaris = []

def menu_input():
    while True:
        try:
            return int(input("Pilih menu (1-6): "))
        except:
            print("Input harus angka!")

def tampil_barang():
    if not inventaris:
        print("Belum ada barang.")
    else:
        idx = 0
        for data in inventaris:
            idx +=1
            print(f"ID: {idx} | Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def tambah_barang():
    nama = input("Nama barang: ").lower()

    # Cek apakah nama barang sudah ada
    for item in inventaris:
        if item[0] == nama:
            print("gagal menambahkan barang.Nama barang sudah ada")
            return

    while True:
        harga = input("Harga: ")
        try:
            harga = int(harga)
            break
        except ValueError:
            print("Harga harus berupa angka!")

    while True:
        stok = input("Stok awal: ")
        try:
            stok = int(stok)
            break
        except ValueError:
            print("Stok harus berupa angka!")

    inventaris.append([nama, harga, stok])
    print("Barang berhasil ditambahkan.")

def cari_barang():
    if not inventaris:
        print("Belum ada barang.")
        return
    
    while True:
        try:
            id = int(input("Masukkan ID barang: "))
            if 1 <= id <= len(inventaris):
                print(inventaris[id-1])
                break
            else:
                print("ID tidak ditemukan!")
        except:
            print("ID harus berupa angka!")

def update_stok():
    if not inventaris:
        print("Belum ada barang.")
        return
    
    tampil_barang()

    try:
        id = int(input("Masukkan ID barang: "))
    except:
        print("ID harus berupa angka!")
        return

    if not (1 <= id <= len(inventaris)):
        print("ID tidak ditemukan!")
        return

    barang = inventaris[id-1]

    while True:
        try:
            perubahan = int(input("Masukkan perubahan stok: "))
            break
        except ValueError:
            print("Input stok harus angka!")

    barang[2] += perubahan
    print("Stok berhasil diperbarui!")
    print(f"Stok baru: {barang[2]}")

def hapus_barang():
    if not inventaris:
        print("Belum ada barang.")
        return
    tampil_barang()

    try:
        id = int(input("Masukkan ID barang yang ingin dihapus: "))
    except:
        print("ID harus angka!")
        return

    if not (1 <= id <= len(inventaris)):
        print("ID tidak ditemukan!")
        return
    del inventaris[id-1]
    print("Barang berhasil dihapus")

while True:
    print("===== INVENTARIS GUDANG =====")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilih = menu_input()

    if pilih == 1:
        tampil_barang()
    elif pilih == 2:
        cari_barang()
    elif pilih == 3:
        tambah_barang()
    elif pilih == 4:
        update_stok()
    elif pilih == 5:
        hapus_barang()
    elif pilih == 6:
        print("Keluar.")
        break
    else:
        print("Menu tidak tersedia.")