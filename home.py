from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class home:
    def __init__(self, root):
        self.root = root
        self.root.title("Embot")
        self.root.geometry("1080x615+100+50")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Email-bot\talk_embot.gif")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)


if __name__ == "__main__":
    root = Tk()
    obj = home(root)
    root.mainloop()
