while True:
    print("========= Program Data Sederhana (Pengulangan) ========")
    print("1. Masukkan identitas")
    print("2. Tentang program ini")
    print("3. Keluar")
    print("=======================================================")

    pilihan = input("Pilih menu 1/2/3: ")
    pilihan = pilihan.strip()

    if pilihan == "":
        print("Error: pilihan tidak boleh kosong.")

    elif pilihan == "1":
        nama = input("Masukkan nama anda: ")
        nama = nama.strip()

        alamat = input("Masukkan alamat anda: ")
        alamat = alamat.strip()

        if nama == "":
            print("Error: nama tidak boleh kosong.")
        elif alamat == "":
            print("Error: alamat tidak boleh kosong.")
        else:
            print(f"Selamat, {nama}.")
            print(f"Alamat {alamat} sudah tervalidasi.")

    elif pilihan == "2":
        print("Program ini dibuat untuk latihan while loop dan menu sederhana.")

    elif pilihan == "3":
        print("Program selesai. Sampai jumpa.")
        break

    else:
        print("Error: pilihan menu tidak valid.")