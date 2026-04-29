print("========== Masukkan Data Diri Anda ==========")

nama = input("Masukkan nama anda: ")
nama = nama.strip()

umur_text = input("Masukkan umur anda: ")
umur_text = umur_text.strip()

if nama == "":
    print("Error: nama tidak boleh kosong.")
elif umur_text == "":
    print("Error: umur tidak boleh kosong.")
elif not umur_text.isdigit():
    print("Error: umur harus berupa angka.")
else:
    umur = int(umur_text)

    if umur <= 0:
        print("Error: Umur Harus lebih dari 0.")
    elif umur > 120:
        print("Error: umur terlalu besar")
    else:
        print(f"Halo, {nama}.")
        print(f"Umur anda adalah {umur} tahun.")
        print("Data anda berhasil diproses.")