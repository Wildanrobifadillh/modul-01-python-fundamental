while True:
    print("============= Menu Pembelian ===================")
    print("1. Input Pembelian")
    print("2. Tentang program")
    print("3. Keluar")
    print("===============================================")

    pilihan = input("Pilih daftar menu 1/2/3: ")
    pilihan = pilihan.strip()

    if pilihan == "":
        print("Error: pilihan tidak boleh kosong.")

    elif pilihan == "1":
        print("============== Input Pembelian ===========")

        nama = input("Masukkan nama anda: ")
        nama = nama.strip()

        nama_barang = input("Masukkan nama barang: ")
        nama_barang = nama_barang.strip()

        harga_barang_text = input("Masukkan harga barang: Rp")
        harga_barang_text = harga_barang_text.strip()

        jumlah_text = input("Masukkan jumlah barang: ")
        jumlah_text = jumlah_text.strip()

        if nama == "":
            print("Error: nama pembeli tidak boleh kosong.")
        elif nama_barang == "":
            print("Error: nama barang tidak boleh kosong.")
        elif harga_barang_text == "":
            print("Error: harga barang tidak boleh kosong.")
        elif jumlah_text == "":
            print("Error: jumlah barang tidak boleh kosong.")
        else:
            try:
                harga_barang = float(harga_barang_text)
                jumlah = int(jumlah_text)

                if harga_barang <= 0:
                    print("Error: harga harus lebih dari 0.")
                elif harga_barang > 100000000:
                    print("Error: harga terlalu besar.")
                elif jumlah <= 0:
                    print("Error: jumlah harus lebih dari 0.")
                elif jumlah > 1000:
                    print("Error: jumlah terlalu banyak.")
                else:
                    total = harga_barang * jumlah

                    print("============ Struk Pembelian ==============")
                    print(f"Pembeli: {nama}")
                    print(f"Nama barang: {nama_barang}")
                    print(f"Harga barang: Rp{harga_barang}")
                    print(f"Jumlah barang: {jumlah}")
                    print(f"Total belanja: Rp{total}")

            except ValueError:
                print("Error: harga harus angka dan jumlah harus angka bulat.")

    elif pilihan == "2":
        print("Program ini dibuat untuk latihan if/elif/else, try/except, dan while.")

    elif pilihan == "3":
        print("Program selesai. Sampai jumpa.")
        break

    else:
        print("Error: pilihan menu tidak valid.")