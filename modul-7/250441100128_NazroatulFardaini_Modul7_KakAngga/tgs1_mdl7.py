kontak = []   

def menu_input():
    while True:
        try:
            pilihan = int(input("Pilih menu (1-6): "))
            return pilihan
        except:
            print("Input harus angka!")


def tampilkan():
    if not kontak:
        print("Belum ada kontak.")
    else:
        print("=== DAFTAR KONTAK ===")
        i = 0
        for data in kontak:
            i += 1
            print(f"{i}. Nama: {data['nama']}, Telp: {data['telp']}, Email: {data['email']}")
        print()


def tambah():
    try:
        while True :
                nama = input("nama: ")
                ada_angka = False
                for karakter in nama:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break
        for data in kontak:
            if data["nama"].lower() == nama.lower():
                print("Gagal menambah kontak! Nama sudah ada.")
                return
            
        while True:
            telp = input("Telepon: ")
            try:
                int(telp)  
                break     
            except ValueError:
                print("Telepon hanya boleh angka! Coba lagi.")
        for data in kontak:
            if data["telp"] == telp:
                print("Gagal menambah kontak! Nomor telepon sudah ada.")
                return
            
        email = input("Email: ")
        for data in kontak:
            if data["email"].lower() == email.lower():
                print("Gagal menambah kontak! Email sudah ada.")
                return
        
        kontak.append({"nama": nama, "telp": telp, "email": email})
        print("Kontak berhasil ditambah.")
    except:
        print("Gagal menambah kontak!")

def cari():
    if not kontak:
        print("Belum ada kontak!")
        return

    tampilkan()

    try:
        while True:
            try:
               nomor = int(input("Masukkan nomor urut yang dicari: "))
               break
            except ValueError:
               print("Input nomor urut harus berupa angka!")
        data = kontak[nomor - 1]
        print(f"Data ditemukan: Nama={data['nama']}, Telp={data['telp']}, Email={data['email']}")
    except:
        print("Nomor kontak tidak ditemukan!")

def update_kontak():
    if not kontak:
        print("Belum ada kontak!")
        return

    tampilkan()

    try:
        while True:
            try:
               nomor = int(input("Masukkan nomor urut yang dicari: "))
               break
            except ValueError:
               print("Input nomor urut harus berupa angka!")

        data = kontak[nomor - 1]

        print(f"=== Update Kontak ===")
        while True :
                nama_baru = input("nama: ")
                ada_angka = False
                for karakter in nama_baru:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break
        while True:
            telpon_baru = input("Telepon: ")
            try:
                int(telpon_baru)  
                break     
            except ValueError:
                print("Telepon hanya boleh angka! Coba lagi.")

        email_baru = input("Email baru: ")

        # Simpan perubahan
        data['nama'] = nama_baru
        data['telp'] = telpon_baru
        data['email'] = email_baru

        print("Kontak berhasil diperbarui.")

    except:
        print("Gagal mengupdate kontak! Nomor tidak valid.")

def hapus():
    if not kontak:
        print("Belum ada kontak!")
        return

    tampilkan()

    try:
        while True:
            try:
               nomor = int(input("Masukkan nomor urut yang dicari: "))
               break
            except ValueError:
               print("Input nomor urut harus berupa angka!")
        kontak.pop(nomor - 1)
        print("Kontak berhasil dihapus.")
    except:
        print("Gagal menghapus! Nomor tidak valid.")

while True:
    print("===== CONTACT BOOK =====")
    print("1. Tampilkan Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilih = menu_input()

    if pilih == 1:
        tampilkan()
    elif pilih == 2:
        cari()
    elif pilih == 3:
        tambah()
    elif pilih == 4:
        update_kontak()
    elif pilih == 5:
        hapus()
    elif pilih == 6:
        print("Keluar")
        break
    else:
        print("Menu tidak tersedia.")