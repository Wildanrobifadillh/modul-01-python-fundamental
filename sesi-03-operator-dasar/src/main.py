print("========== Masukkan Data Diri Anda ==========")

nama = input("Masukkan nama anda: ")
nama = nama.strip()

umur_text = input("Masukkan umur anda: ")
umur_text = umur_text.strip()

tahun_sekarang_text = input ("Masukan tahun sekarang : ")
tahun_sekarang_text = tahun_sekarang_text.strip()

if nama == "":
    print("Error: nama tidak boleh kosong.")
elif umur_text == "":
    print("Error: umur tidak boleh kosong.")
elif tahun_sekarang_text =="":
    print("Error: tahun tidak boleh kosong.")
elif not umur_text.isdigit():
    print("Error: umur harus berupa angka.")
elif not tahun_sekarang_text.isdigit():
    print("Error : tahun harus berupa angka")

else:
    umur = int(umur_text)
    tahun_sekarng = int(tahun_sekarang_text)

    if umur <= 0:
        print("Error: Umur Harus lebih dari 0.")
    elif umur > 120:
        print("Error: umur terlalu besar")
    elif tahun_sekarng < 1900:
        print("Error : tahun sekarng tidak masuk akal")

    else:
        tahun_lahir = tahun_sekarng - umur

        print(f"Halo, {nama}.")
        print(f"perkiraan tahun lahir anda adalah {tahun_lahir}.")