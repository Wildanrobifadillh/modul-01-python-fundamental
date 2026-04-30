while True:
    print("============Metode Pengulangan=============")

    nama = input("Masukan nama anda: ")
    nama = nama.strip()

    umur_text = input("Masukan umur anda: ")
    umur_text = umur_text.strip()

    if nama =="":
        print("Error: nama tidak boleh kosong.")
    elif umur_text == "":
        print("Error: umur tidak boleh kosong.")
    elif not umur_text.isdigit():
        print("Error: umur harus berupa angka.")
    
    else:
        umur = int(umur_text)

        if umur <= 0:
            print("Error: umur harus lebih dari 0.")
        elif umur > 120:
            print("Error: umur terlalu besar.")
        else:
            print("=================Notifikasi===================")
            print(f"Selamat!!, {nama} kamu memenuhi syarat.")
            print(f"umur anda valid: {umur} tahun.")
            print("==============================================")
            break