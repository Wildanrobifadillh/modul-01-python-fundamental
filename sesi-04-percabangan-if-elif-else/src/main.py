print("=============Program Kategori Umur===============")

nama = input ("masukan nama anda : ")
nama = nama.strip()

umur_text = input("masukan umur anda: ")
umur_text = umur_text.strip()

if nama =="":
    print("Error : nama tidak boleh kosong.")
elif umur_text =="":
    print("Error : umur tidak boleh kosong.")
elif not umur_text.isdigit():
    print("Error : Umur harus berupa angka.")

else:
    umur = int(umur_text)

    if umur <= 0 :
        print("Error ; umur harus lebih dari 0.")
    elif umur > 120 :
        print("Error : umur terlalu besar")
    elif umur <= 12 :
        print(f"Hallo, {nama}")
        print("Kategori umur anda : anak-anak")
    elif umur <= 18 :
        print(f"Halo, {nama}")
        print("Kategori umur anda : remaja")
    elif umur <= 59 :
        print(f"Halo, {nama}.")
        print("Kategori umur anda : dewasa")
    elif umur >= 59 :
        print(f"Halo, {nama}.")
        print("Kategori umur anda : lansia")
    else:
        print(f"Halo, {nama}.")
        print(f"kategori umur anda : lansia.")

