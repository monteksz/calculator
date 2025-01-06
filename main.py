def calculator():
    print("\n--- Kalkulator Sederhana ---")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # Memilih operasi
    try:
        choice = int(input("Masukkan pilihan (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            return calculator()

        # Memasukkan angka
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        # Melakukan operasi
        if choice == 1:
            result = num1 + num2
            operator = '+'
        elif choice == 2:
            result = num1 - num2
            operator = '-'
        elif choice == 3:
            result = num1 * num2
            operator = '*'
        elif choice == 4:
            if num2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                return calculator()
            result = num1 / num2
            operator = '/'

        # Menampilkan hasil
        print(f"Hasil: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")
        calculator()

if __name__ == "__main__":
    calculator()