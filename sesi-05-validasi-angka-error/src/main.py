print("============ Validasi Harga Barang ==============")

nama_pembeli = input("Masukkan nama anda: ")
nama_pembeli = nama_pembeli.strip()

nama_barang = input("Masukkan nama barang: ")
nama_barang = nama_barang.strip()

harga_barang_text = input("Masukkan harga barang: Rp")
harga_barang_text = harga_barang_text.strip()

jumlah_text = input("Masukkan jumlah barang: ")
jumlah_text = jumlah_text.strip()

if nama_pembeli == "":
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
            print("Error: harga barang harus lebih dari 0.")
        elif harga_barang > 1000000000:
            print("Error: harga barang terlalu besar.")
        elif jumlah <= 0:
            print("Error: jumlah barang harus lebih dari 0.")
        elif jumlah > 1000:
            print("Error: jumlah barang terlalu banyak.")
        else:
            total = harga_barang * jumlah

            print("============ Detail Barang ===========")
            print(f"Nama pelanggan: {nama_pembeli}")
            print(f"Nama barang: {nama_barang}")
            print(f"Harga barang: Rp.{harga_barang}")
            print(f"Jumlah barang: {jumlah} QTY")
            print(f"Total harga: Rp{total}")

    except ValueError:
        print("Error: harga harus angka dan jumlah harus angka bulat.")