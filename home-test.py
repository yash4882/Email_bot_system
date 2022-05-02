from email.mime import image
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence


class home:


    def __init__(self, root):
        self.root = root
        self.root.title("Embot-Home")
        self.root.geometry("1080x615+100+50")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\HP\OneDrive\Desktop\Email-bot\talk_embot.gif")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        Button(cursor="hand2", text="Start", bd=0.5, font=(
            "Century", 13), fg="black", bg="white smoke",).place(x=400, y=520, width=150, height=35)

        Button(cursor="hand2", text="Exit", bd=0.5, font=(
            "Century", 13), fg="black", bg="white smoke", command=exit).place(x=540, y=520, width=150, height=35)


if __name__ == "__main__":
    root = Tk()
    obj = home(root)
    root.mainloop()
