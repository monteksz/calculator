import tkinter as tk
from tkinter import messagebox

# Fungsi untuk melakukan perhitungan
def perform_calculation():
    try:
        # Mengambil input angka dan operasi
        numbers = [float(entry.get()) for entry in additional_entries]
        operation = operation_var.get()

        result = numbers[0]
        step = f"{numbers[0]}"

        for num in numbers[1:]:
            if operation == "+":
                result += num
                step += f" + {num}"
            elif operation == "-":
                result -= num
                step += f" - {num}"
            elif operation == "*":
                result *= num
                step += f" * {num}"
            elif operation == "/":
                if num == 0:
                    messagebox.showerror("Error", "Pembagian dengan nol tidak diperbolehkan.")
                    return
                result /= num
                step += f" / {num}"

        step += f" = {result}"

        # Menampilkan hasil dan langkah
        result_label.config(text=f"Hasil: {result}")
        steps_text.insert(tk.END, step + "\n")

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid. Masukkan angka yang benar.")

# Fungsi untuk menambah kolom angka tambahan
def add_number_field():
    new_row = len(additional_entries)
    label = tk.Label(main_frame, text=f"Angka ke-{new_row + 1}:")
    label.grid(row=new_row + 1, column=0, padx=10, pady=5)
    entry = tk.Entry(main_frame)
    entry.grid(row=new_row + 1, column=1, padx=10, pady=5)
    additional_entries.append(entry)

    # Pindahkan tombol "Tambah Angka" ke bawah
    add_num_button.grid(row=new_row + 2, column=0, columnspan=2, pady=10)

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Sederhana dengan Penambahan Dinamis")

# Frame utama
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

# Label dan entry untuk angka pertama
label_num1 = tk.Label(main_frame, text="Angka ke-1:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(main_frame)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Menyimpan kolom angka tambahan
additional_entries = [entry_num1]

# Tombol untuk menambah kolom angka tambahan
add_num_button = tk.Button(main_frame, text="Tambah Angka", command=add_number_field)
add_num_button.grid(row=1, column=0, columnspan=2, pady=10)

# Tombol hitung
calculate_button = tk.Button(root, text="Hitung", command=perform_calculation)
calculate_button.pack(pady=10)

# Label hasil
result_label = tk.Label(root, text="Hasil:", font=("Arial", 12))
result_label.pack(pady=5)

# Pilihan operasi
operation_var = tk.StringVar(value="+")
operation_label = tk.Label(root, text="Operasi:")
operation_label.pack(pady=5)
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack(pady=5)

# Kotak teks untuk history langkah-langkah
steps_label = tk.Label(root, text="History Langkah-Langkah:")
steps_label.pack()
steps_text = tk.Text(root, height=10, width=30)
steps_text.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
