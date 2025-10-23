# kalkulator.py
# Aplikasi Kalkulator Sederhana
# Dibuat untuk latihan GitHub

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol!"
    return a / b

def main():
    print("=== KALKULATOR SEDERHANA ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    pilihan = input("Pilih operasi (1/2/3/4): ")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = tambah(a, b)
        operasi = "+"
    elif pilihan == "2":
        hasil = kurang(a, b)
        operasi = "-"
    elif pilihan == "3":
        hasil = kali(a, b)
        operasi = "×"
    elif pilihan == "4":
        hasil = bagi(a, b)
        operasi = "÷"
    else:
        print("Pilihan tidak valid.")
        return

    print(f"Hasil dari {a} {operasi} {b} = {hasil}")

if __name__ == "__main__":
    main()
