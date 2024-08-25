# Daftar belanjaan yang disimpan dalam list
belanjaan = ["wortel", "telur", "singkong"]

def tampilkan_belanjaan():
    if not belanjaan:
        print("Tidak ada belanjaan yang tercatat.")
    else:
        print("Daftar Belanjaan:")
        for index, item in enumerate(belanjaan, start=1):
            print(f"{index}. {item}")

def tambah_belanjaan():
    item = input("Masukkan nama barang yang ingin ditambahkan: ")
    belanjaan.append(item)
    print(f"{item} telah ditambahkan ke daftar belanja.")

def hapus_belanjaan():
    tampilkan_belanjaan()
    if belanjaan:
        try:
            nomor = int(input("Masukkan nomor barang yang ingin dihapus: "))
            if 0 < nomor <= len(belanjaan):
                item = belanjaan.pop(nomor - 1)
                print(f"{item} telah dihapus dari daftar belanja.")
            else:
                print("Nomor tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka")

def menu():
    print("\n=== Pengelola Belanja ===")
    print("1. Tampilkan Belanjaan")
    print("2. Tambah Belanjaan")
    print("3. Hapus Belanjaan")
    print("4. Keluar")
    pilihan = input("Pilih menu: ").strip()
    return pilihan

def main():
    print("Program dimulai")
    while True:
        pilihan = menu()
        print(f"Pilihan yang diproses: '{pilihan}'")
        if pilihan == '1':
            tampilkan_belanjaan()
        elif pilihan == '2':
            tambah_belanjaan()
        elif pilihan == '3':
            hapus_belanjaan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan pengelola belanja.")
            break
        else:
            print(f"Pilihan '{pilihan}' tidak dikenal. Silakan masukkan angka 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()