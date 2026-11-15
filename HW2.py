import tkinter as tk
from PIL import Image, ImageTk


def show_image():
    label.config(image=my_img)

root = tk.Tk()
root.title("RPS Game")
#root.geometry("400x400")
my_img = tk.PhotoImage(file="Rc.png")
label = tk.Label(root)
label.pack()


btn = tk.Button(root, text="Rock", command=show_image)
btn.pack()

def show_image2():
    label.config(image=my_img2)
my_img2 = tk.PhotoImage(file="Untitled.png")
btn = tk.Button(root, text="Paper", command=show_image2)
btn.pack()

def show_image3():
    label.config(image=my_img3)
my_img3 = tk.PhotoImage(file="Sc.png")
btn = tk.Button(root, text="Scissors", command=show_image3)
btn.pack()

import random
choices = [show_image(), show_image2(),show_image3()]
pc_choice = random.choice(choices)
def show_imageall():
    label.config(image=my_img)
    pc_pick = random.choice([my_img,my_img2,my_img3])
    print("PC chose:", pc_pick)