import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        # Mengambil input angka dan operasi
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        # Proses operasi
        if operation == "+":
            result = num1 + num2
            step = f"{num1} + {num2} = {result}"
        elif operation == "-":
            result = num1 - num2
            step = f"{num1} - {num2} = {result}"
        elif operation == "*":
            result = num1 * num2
            step = f"{num1} * {num2} = {result}"
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diperbolehkan.")
                return
            result = num1 / num2
            step = f"{num1} / {num2} = {result}"
        else:
            messagebox.showerror("Error", "Operasi tidak valid.")
            return

        # Menampilkan hasil dan langkah
        result_label.config(text=f"Hasil: {result}")
        steps_text.insert(tk.END, step + "\n")

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid. Masukkan angka yang benar.")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Label dan entry untuk angka pertama
label_num1 = tk.Label(root, text="Angka Pertama:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Label dan entry untuk angka kedua
label_num2 = tk.Label(root, text="Angka Kedua:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Pilihan operasi
operation_var = tk.StringVar(value="+")
operation_label = tk.Label(root, text="Operasi:")
operation_label.grid(row=2, column=0, padx=10, pady=5)
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Tombol hitung
calculate_button = tk.Button(root, text="Hitung", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label hasil
result_label = tk.Label(root, text="Hasil:", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Kotak teks untuk History
steps_label = tk.Label(root, text="History")
steps_label.grid(row=5, column=0, columnspan=2)
steps_text = tk.Text(root, height=10, width=30)
steps_text.grid(row=6, column=0, columnspan=2, pady=5)

# Menjalankan aplikasi
root.mainloop()