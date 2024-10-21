import re
from tabulate import tabulate

data_buku = [
    {
        'ISBN': 9788184759334,
        'Buku': 'Laskar Pelangi',
        'Penulis': 'Andrea Hirata',
        'Stok Buku': 5,
        'Tahun Terbit': 2005
    },
    {
        'ISBN': 9781399405959,
        'Buku': 'How to Think Like a Philosopher',
        'Penulis': 'Peter Cave',
        'Stok Buku': 3,
        'Tahun Terbit': 2011
    },
    {
        'ISBN': 9786233463034,
        'Buku': 'The Alchemist',
        'Penulis': 'Paulo Coelho',
        'Stok Buku': 2,
        'Tahun Terbit': 1988
    }
]

data_penyewa = [
    {
        'Nama': 'Andi',
        'ISBN': 9788184759334,
        'NIK': 3271065412990001
    },
    {
        'Nama': 'Budi',
        'ISBN': 9781399405959,
        'NIK': 6102041105012345
    }
]

buku_disewa = [
    {
        'ISBN': 9788184759334,
        'Buku': 'Laskar Pelangi',
        'Penulis': 'Andrea Hirata',
        'Jumlah Buku': 1
    },
    {
        'ISBN': 9781399405959,
        'Buku': 'How to Think Like a Philosopher',
        'Penulis': 'Peter Cave',
        'Jumlah Buku': 1
    }
]

arsip_data_buku = []
# Kumpulan Fungsi print data
def print_data_kosong():
    print("\n\033[31mData tidak ditemukan.\033[0m")

def show_data():
    if not data_buku:
        print_data_kosong()
        return
    if data_buku:
        print(tabulate(data_buku, headers='keys', tablefmt='fancy_grid'))

def show_data_penyewa():
    if not data_penyewa:
        print_data_kosong()
        return
    if data_penyewa:
        print(tabulate(data_penyewa, headers='keys', tablefmt='fancy_grid'))

def show_data_buku_disewa():
    if not buku_disewa:
        print_data_kosong()
        return
    if buku_disewa:
        print(tabulate(buku_disewa, headers='keys', tablefmt='fancy_grid'))

def show_arsip_buku():
    if not arsip_data_buku:
        print_data_kosong()
        return
    if arsip_data_buku:
        print(tabulate(arsip_data_buku, headers='keys', tablefmt='fancy_grid'))
# Kumpulan fungsi input 
def input_name(prompt):
    while True:
        name = input(prompt).strip().title()  
        if is_valid_name(name):
            return name
        else:
            print("\033[31mInput hanya boleh berisi huruf, titik (.), tanda kutip tunggal (') dan spasi yang valid.\033[0m")

def input_angka(prompt):
    while True:
        number = input(prompt).strip()
        if number.isdigit():
            return int(number)
        else:
            print("\033[31mInput harus berupa angka.\033[0m")
def input_stok_buku():
    while True:
        try:
            stok = int(input("Masukkan jumlah stok buku: ").strip())
            if stok <= 0:
                print("\033[31mJumlah stok tidak boleh 0 atau negatif. Silakan masukkan stok yang valid.\033[0m")
            else:
                return stok
        except ValueError:
            print("\033[31mInput tidak valid! Harap masukkan angka.\033[0m")

def input_tahun_terbit():
    while True:
        try:
            tahun = int(input("Masukkan tahun terbit: ").strip())
            if tahun < 1900 or tahun > 2024:
                print(f"\033[31mTahun terbit harus antara 1900 hingga 2024. Silakan coba lagi.\033[0m")
            else:
                return tahun
        except ValueError:
            print("\033[31mInput tidak valid! Harap masukkan angka.\033[0m")

# Fungsi untuk cek dan input dengan validasi
def cek_isbn():
    while True:
        isbn = input("Masukkan ISBN dengan format 10-13 digit dan diawali angka 97: ")
        if re.fullmatch(r"97\d{8,11}", isbn):
            return int(isbn)
        else:
            print("\033[31mInput ISBN tidak valid. Silakan coba lagi.\033[0m")

def cek_nik():
    while True:
        nik = input("Masukkan NIK : ")
        if re.fullmatch(r"\d{16}", nik):
            return int(nik)
        else:
            print("\033[31mInput NIK tidak valid. Silakan coba lagi.\033[0m")

# Fungsi untuk cek duplikasi ISBN
def is_duplicate_ISBN(isbn):
    for buku in data_buku:
        if buku["ISBN"] == isbn:
            return True
    return False

def is_valid_name(name):
    for char in name:
        if not (char.isalpha() or char in {'.', "'"} or char == ' '):
            return False
    return True

# Fungsi Sub Menu Read Data
def search_data():
    print("\n\033[34mSearch data berdasarkan: \033[0m\n")
    print("1. Judul Buku")
    print("2. Penulis")

    pilihan = input_angka("Pilih Opsi: ")

    if pilihan == 1:
        keyword = input("Masukkan judul buku: ").strip().lower()
        filtered_data = [buku for buku in data_buku if keyword in buku['Buku'].lower()]
    elif pilihan == 2:
        keyword = input("Masukkan nama penulis: ").strip().lower()
        filtered_data = [buku for buku in data_buku if keyword in buku['Penulis'].lower()]
    else:
        print("\033[31mPilihan tidak valid.\033[0m")
        return

    if filtered_data:
        print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
    else:
        print("\033[31mTidak ada data yang sesuai dengan search data.\033[0m")

# Fungsi sort data
def sort_data():
    print("\n=== SORT DATA ===")
    print("\n\033[34mPilih kriteria pengurutan: \033[0m\n")
    print("1. Urutkan berdasarkan Judul Buku")
    print("2. Urutkan berdasarkan Nama Penulis")
    print("3. Urutkan berdasarkan Nomor ISBN")
    print("4. Urutkan berdasarkan Stok Buku")
    print("5. Urutkan berdasarkan Tahun Terbit")
    print("0. Kembali ke Sub Menu")

    pilihan = input_angka("Pilih Opsi: ")

    if pilihan == 1:
        sorted_data = sorted(data_buku, key=lambda x: x['Buku'])
    elif pilihan == 2:
        sorted_data = sorted(data_buku, key=lambda x: x['Penulis'])
    elif pilihan == 3:
        sorted_data = sorted(data_buku, key=lambda x: x['ISBN'])
    elif pilihan == 4:
        sorted_data = sorted(data_buku, key=lambda x: x['Stok Buku'])
    elif pilihan == 5:
        sorted_data = sorted(data_buku, key=lambda x: x['Tahun Terbit'])
    elif pilihan == 0:
        return True 
    else:
        print("\033[31mPilihan tidak valid.\033[0m")
        return True 

    print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
    return True  

# Fungsi Read Data
def read_data():
    while True:
        print("\n=== READ DATA ===")
        print("\n\033[34mSilahkan pilih opsi dibawah ini: \033[0m\n")
        print("1. Lihat Daftar Buku")
        print("2. Lihat Data Penyewa")
        print("3. Lihat Data Buku Disewa")
        print("4. Lihat Arsip Buku")
        print("0. Kembali ke Menu Utama")

        input_user = input("Pilih Opsi: ").strip()

        if input_user == "1":
            show_data()
            while True:
                print("\n=== SUB MENU READ DATA ===")
                print("\n\033[34mSilahkan pilih opsi dibawah ini: \033[0m\n")
                print("1. Urutkan Data")
                print("2. Search Data")
                print("0. Kembali ke Sub Menu")

                input_user = input_angka("Pilih Opsi: ")

                if input_user == 1:
                    if sort_data():
                        continue
                elif input_user == 2:
                    if search_data():
                        continue
                elif input_user == 0:
                    break
                else:
                    print("\033[31mPilihan tidak tersedia, masukkan input sesuai opsi.\033[0m")
        elif input_user == "2":
            show_data_penyewa()
        elif input_user == "3":
            show_data_buku_disewa()
        elif input_user == "4":
            show_arsip_buku()
        elif input_user == "0":
            return
        else:
            print("\033[31mPilihan tidak tersedia, masukkan input sesuai opsi.\033[0m")

# Fungsi Create Data
def create_data():
    print("\n=== CREATE DATA ===")
    show_data()
    print("Silahkan masukkan nomor ISBN buku yang ingin ditambahkan.")
    while True:
        ISBN = cek_isbn()
        if is_duplicate_ISBN(ISBN):
            print("ISBN sudah ada dalam database. Silakan masukkan ISBN yang berbeda.")
            continue

        Buku = input_name("Masukkan judul buku: ")
        Penulis = input_name("Masukkan nama penulis: ")
        Stok_Buku = input_stok_buku()
        Tahun_Terbit = input_tahun_terbit()
        data_buku.append({
                            "ISBN": ISBN,
                            "Buku": Buku,
                            "Penulis": Penulis,
                            "Stok Buku": Stok_Buku,
                            "Tahun Terbit": Tahun_Terbit
                        })
        print("\n\033[32mData buku berhasil ditambahkan!\033[0m")
        show_data()
        break

# Fungsi Update Data
def update_data():
    print("\n=== UPDATE DATA ===")
    show_data()
    while True:
        print("Silahkan masukkan nomor ISBN buku yang ingin diupdate.")
        inputan = cek_isbn()
        buku_ditemukan = None
        for buku in data_buku:
            if buku["ISBN"] == inputan:
                buku_ditemukan = buku
                break
        if buku_ditemukan:
            break
        else:
            print(f"\033[31mBuku dengan ISBN {inputan} tidak ditemukan. Silakan coba lagi.\033[0m")

    print("\nInformasi Buku yang Akan Diupdate: ")
    print(tabulate([buku_ditemukan], headers='keys', tablefmt='fancy_grid'))

    while True:
        print("\n=== SUB MENU UPDATE DATA ===")
        print("\nPilih Opsi yang ingin diupdate:")
        print("1. Judul Buku")
        print("2. Penulis")
        print("3. Stok Buku")
        print("4. Tahun Terbit")
        print("0. Kembali ke Menu Utama")

        pilihan = input_angka("Masukkan nomor opsi yang ingin diupdate: ")

        if pilihan == 1:
            Buku = input_name("Masukkan judul buku baru: ")
            buku_ditemukan["Buku"] = Buku
            print("\033[32mData buku berhasil diperbarui!\033[0m")
            show_data()
        elif pilihan == 2:
            Penulis = input_name("Masukkan nama penulis baru: ")
            buku_ditemukan["Penulis"] = Penulis
            print("\033[32mData buku berhasil diperbarui!\033[0m")
            show_data()
        elif pilihan == 3:
            Stok_Buku = input_stok_buku()
            buku_ditemukan["Stok Buku"] = int(Stok_Buku)
            print("\033[32mData buku berhasil diperbarui!\033[0m")
            show_data()
        elif pilihan == 4:
            Tahun_Terbit = input_tahun_terbit()
            buku_ditemukan["Tahun Terbit"] = int(Tahun_Terbit)
            print("\033[32mData buku berhasil diperbarui!\033[0m")
            show_data()
        elif pilihan == 0:
            print("Kembali ke menu utama.")
            break
        else:
            print("\033[31mPilihan tidak valid. Silakan coba lagi.\033[0m")
            continue

# Fungsi Delete Data
from tabulate import tabulate

def delete_data():
    while True:
        print("\n=== DELETE DATA ===")
        show_data()  

        print("Silahkan masukkan nomor ISBN buku yang ingin dihapus.")
        isbn = cek_isbn()  

        for buku in data_buku:
            if buku["ISBN"] == isbn:
                keys = ["ISBN", "Judul Buku", "Penulis", "Stok Buku", "Tahun Terbit"]
                buku_data = [[
                    buku["ISBN"],
                    buku["Buku"],
                    buku["Penulis"],
                    buku["Stok Buku"],
                    buku["Tahun Terbit"]
                ]]
                print("\nBuku yang akan dihapus:")
                print(tabulate(buku_data, headers=keys, tablefmt="fancy_grid"))

                konfirmasi = input("\033[33mApakah Anda yakin ingin menghapus buku ini? (Y/N): \033[0m").strip().upper()
                if konfirmasi == 'Y':
                    data_buku.remove(buku) 
                    arsip_data_buku.append(buku) 
                    print(f"\033[32mData buku dengan ISBN {isbn} berhasil dihapus dan dipindahkan ke arsip!\033[0m")
                    return
                elif konfirmasi == 'N':
                    print("\033[33mPenghapusan dibatalkan.\033[0m")
                    return
                else:
                    print("\033[31mInput tidak valid. Silakan masukkan 'Y' atau 'N'.\033[0m")
                    continue
        print(f"\033[31mBuku dengan ISBN {isbn} tidak ditemukan. Silakan coba lagi.\033[0m")


# Fungsi Sewa Buku
def sewa_buku():
    print("\n=== SEWA BUKU ===")
    show_data()
    nik = cek_nik()
    for penyewa in data_penyewa:
        if penyewa['NIK'] == nik and penyewa['ISBN'] == isbn:
            print("\033[31mAnda sudah menyewa buku. Tidak dapat menyewa lebih dari satu kali.\033[0m")
            return
    nama = input_name("Masukkan nama anda: ")
    print("Silahkan masukkan nomor ISBN buku yang ingin disewa.")
    isbn = cek_isbn()

    for buku in data_buku:
        if buku["ISBN"] == isbn:
            if buku["Stok Buku"] > 0:
                buku["Stok Buku"] -= 1

                for b in buku_disewa:
                    if b["ISBN"] == isbn:
                        b["Jumlah Buku"] += 1
                        break
                else:
                    buku_disewa.append({
                                        'ISBN': isbn,
                                        'Buku': buku['Buku'],
                                        'Penulis': buku['Penulis'],
                                        'Jumlah Buku': 1
                                       })
                data_penyewa.append({
                                    'Nama': nama,
                                    'ISBN': isbn,
                                    'NIK': nik
                                    })
                print(f"\033[32mBuku dengan ISBN {isbn} berhasil disewa!\033[0m")
                return
            else:
                print(f"\033[31mStok buku dengan ISBN {isbn} habis.\033[0m")
                return
    else:
        print(f"\033[31mTidak ditemukan buku dengan ISBN {isbn}. Silakan coba lagi.\033[0m")

# Fungsi Kembalikan Buku
def kembalikan_buku():
    print("\n=== KEMBALIKAN BUKU ===")
    show_data_penyewa()
    nik = cek_nik()
    penyewa_dipilih = [penyewa for penyewa in data_penyewa if penyewa["NIK"] == nik]

    if penyewa_dipilih:
        print(tabulate(penyewa_dipilih, headers="keys", tablefmt="fancy_grid"))
        for penyewa in penyewa_dipilih:
            isbn = penyewa["ISBN"]
            for buku in data_buku:
                if buku["ISBN"] == isbn:
                    buku["Stok Buku"] += 1
                    data_penyewa.remove(penyewa)
                    print(f"\033[32mBuku dengan ISBN {isbn} berhasil dikembalikan!\033[0m")
                    return
            print(f"\033[31mBuku dengan ISBN {isbn} tidak ditemukan di database.\033[0m")
            return
    else:
        print(f"\033[31mTidak ditemukan penyewa dengan NIK {nik}. Silakan coba lagi.\033[0m")


# # # # MAIN MENU # # # #
def main_menu():
    print('\n=========== Selamat Datang di Perpustakaan Purwadhika! ==========')
    while True:
        print("\n=== MAIN MENU ===")
        print("\n\033[34mSilahkan pilih opsi dibawah ini: \033[0m\n")
        print('1. Lihat Data Perpustakaan')
        print('2. Tambah Buku')
        print('3. Update Buku')
        print('4. Hapus Buku')
        print('5. Sewa Buku')
        print('6. Kembalikan Buku')
        print('0. Keluar')

        user_input = input('\nPilih Opsi :')

        if user_input == '1':
            read_data()
        elif user_input == '2':
            create_data()
        elif user_input == '3':
            update_data()
        elif user_input == '4':
            delete_data()
        elif user_input == '5':
            sewa_buku()
        elif user_input == '6':
            kembalikan_buku()
        elif user_input == '0':
            print('\n==== Terima kasih telah menggunakan Perpustakaan Purwadhika! ====\n')
            return
        else:
            print("\033[31mPilihan tidak tersedia, masukkan input sesuai opsi.\033[0m")

main_menu()
