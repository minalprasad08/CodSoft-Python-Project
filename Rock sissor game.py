import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.configure(bg="#222222")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="#ffffff", bg="#222222")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#222222")
frame.pack()

btn_rock = tk.Button(frame, text="Rock", font=("Arial", 14, "bold"), fg="#ffffff", bg="#ff5733", width=10, height=2, command=lambda: play("Rock"))
btn_rock.grid(row=0, column=0, padx=10, pady=10)

btn_paper = tk.Button(frame, text="Paper", font=("Arial", 14, "bold"), fg="#ffffff", bg="#33c1ff", width=10, height=2, command=lambda: play("Paper"))
btn_paper.grid(row=0, column=1, padx=10, pady=10)

btn_scissors = tk.Button(frame, text="Scissors", font=("Arial", 14, "bold"), fg="#ffffff", bg="#33ff57", width=10, height=2, command=lambda: play("Scissors"))
btn_scissors.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
