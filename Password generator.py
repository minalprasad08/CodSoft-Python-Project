import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if numbers_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        check_password_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def check_password_strength(password):
    length = len(password)
    strength_label.config(fg="white", bg="black")

    if length < 6:
        strength_label.config(text="Weak Password ❌", fg="red")
    elif length < 10:
        strength_label.config(text="Moderate Password ⚠️", fg="orange")
    else:
        strength_label.config(text="Strong Password ✅", fg="green")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="black")

header_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="black")
header_label.pack(pady=10)

tk.Label(root, text="Password Length:", fg="white", bg="black").pack()
length_entry = tk.Entry(root, bg="white", fg="black")
length_entry.pack()

uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

check_frame = tk.Frame(root, bg="black")
check_frame.pack(pady=5)

uppercase_checkbox = tk.Checkbutton(check_frame, text="Uppercase Letters", variable=uppercase_var, bg="black", fg="white")
numbers_checkbox = tk.Checkbutton(check_frame, text="Include Numbers", variable=numbers_var, bg="black", fg="white")
special_checkbox = tk.Checkbutton(check_frame, text="Special Characters", variable=special_var, bg="black", fg="white")

uppercase_checkbox.pack(anchor="w")
numbers_checkbox.pack(anchor="w")
special_checkbox.pack(anchor="w")

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="white", fg="black", font=("Arial", 12, "bold"))
generate_btn.pack(pady=5)

password_entry = tk.Entry(root, width=30, font=("Arial", 12), bg="white", fg="black")
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="black")
strength_label.pack(pady=5)

root.mainloop()
