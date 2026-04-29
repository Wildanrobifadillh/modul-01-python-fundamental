nama = input("masukan nama anda : ")
nama = nama.strip()

umur_text = input("masukan umur anda : ")
umur = umur_text.strip()

tahun_sekarang_text = input("masukan tahun sekarang : ")
tahun_sekarang_text = tahun_sekarang_text.strip()

if nama == "":
    print("Error= nama tidak boleh kosong.")
elif umur_text == "":
    print("Error : umur tidak boleh kosong.")
elif tahun_sekarang_text == "":
    print("Error : tahun tidak boleh kosong.")
elif not umur_text.isdigit():
    print("Error : umur harus berupa angka.")
elif not tahun_sekarang_text.isdigit():
    print("Error: tahun ssekarang harus berupa angka.")

else:
    umur = int(umur_text)
    tahun_sekarang = int(tahun_sekarang_text)

    if umur <= 0 :
        print("Error : umur harus lebih dari 0.")
    elif umur >= 120 :
        print("Error : umur terlalu besar.")
    elif tahun_sekarang < 1900 :
        print("Error: tahun tidak masuk akal")
    
    else:
        tahun_lahir = tahun_sekarang - umur

        print(f"Halo, {nama}.")
        print(f"Umur anda adalah {umur} tahun.")
        print(f"perkiraan tahun lahir anda adalah {tahun_lahir}. ")