print("============ Program Nilai Siswa ===============")

nama = input("Masukkan nama siswa: ")
nama = nama.strip()

nilai_text = input("Masukkan nilai siswa: ")
nilai_text = nilai_text.strip()

if nama == "":
    print("Error: nama siswa tidak boleh kosong.")
elif nilai_text == "":
    print("Error: nilai siswa tidak boleh kosong.")
elif not nilai_text.isdigit():
    print("Error: nilai siswa harus berupa angka.")
else:
    nilai = int(nilai_text)

    if nilai < 0:
        print("Error: nilai siswa tidak boleh kurang dari 0.")
    elif nilai > 100:
        print("Error: nilai siswa tidak boleh lebih dari 100.")
    elif nilai >= 90:
        print(f"Nama siswa: {nama}")
        print(f"Nilai: {nilai}")
        print("Grade: A")
    elif nilai >= 80:
        print(f"Nama siswa: {nama}")
        print(f"Nilai: {nilai}")
        print("Grade: B")
    elif nilai >= 70:
        print(f"Nama siswa: {nama}")
        print(f"Nilai: {nilai}")
        print("Grade: C")
    elif nilai >= 60:
        print(f"Nama siswa: {nama}")
        print(f"Nilai: {nilai}")
        print("Grade: D")
    else:
        print(f"Nama siswa: {nama}")
        print(f"Nilai: {nilai}")
        print("Grade: E")