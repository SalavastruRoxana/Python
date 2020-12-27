import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        #Frame
        canvas = tk.Canvas(root, height=700, width=900)
        canvas.pack()
        self.frame = tk.Frame(root, bg='light cyan')
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        # Dropdown button pentru selectare categorii
        meniu = Menubutton(self.frame, text="Subiecte de interes", relief=RAISED, bg = "coral3")
        meniu.grid()
        meniu.menu = Menu(meniu, tearoff=0)
        meniu["menu"] = meniu.menu
        meniu.place(x = 20, y = 20)

        self.Item0 = IntVar()
        self.Item1 = IntVar()
        self.Item2 = IntVar()
        self.Item3 = IntVar()
        self.Item4 = IntVar()
        self.Item5 = IntVar()

        meniu.menu.add_checkbutton(label="Politica", variable=self.Item0, command = self.Item_test())
        meniu.menu.add_checkbutton(label="Biologie", variable=self.Item1, command=self.Item_test())
        meniu.menu.add_checkbutton(label="Stiri", variable=self.Item2, command=self.Item_test())
        meniu.menu.add_checkbutton(label="Medicina", variable=self.Item3, command=self.Item_test())
        meniu.menu.add_checkbutton(label="Extern", variable=self.Item4, command=self.Item_test())
        meniu.menu.add_checkbutton(label="Mixt", variable=self.Item5, command=self.Item_test())

        # Categoriile preferate
        self.textSubiecteInteres = StringVar()
        self.textSubiecteInteres.set('Nici un subiect de interes selectat')
        self.categoriiSelectate = Label(self.frame, height = 2, width = 50, bd = 5, textvariable = self.textSubiecteInteres, bg = "SkyBlue3")
        self.categoriiSelectate.pack(padx=5, pady=5, side=tk.TOP)

        self.actualizeaza = Button(self.frame, text="Actualizeaza subiecte de interes", command=self.Item_test)
        self.actualizeaza.pack(padx=2, pady=2)

        #Fereastra cu stiri
        self.fereastraStiri = tk.Frame(self.frame, bg = "light blue")
        self.fereastraStiri.place(relx=0.02, rely=0.18, relwidth=0.935, relheight=0.81)


    def Item_test(self):
        anyItem = False
        subiecte = "Subiectele de interes: "
        if self.Item0.get() == True:
            anyItem = True
            subiecte = subiecte + " Politica "
            self.textSubiecteInteres.set(subiecte)
        if self.Item1.get() == True:
            subiecte = subiecte + " Biologie "
            self.textSubiecteInteres.set(subiecte)
            anyItem = True
        if self.Item2.get() == True:
            subiecte = subiecte + " Stiri "
            self.textSubiecteInteres.set(subiecte)
            anyItem = True
        if self.Item3.get() == True:
            subiecte = subiecte + " Medicina "
            self.textSubiecteInteres.set(subiecte)
            anyItem = True
        if self.Item4.get() == True:
            subiecte = subiecte + " Extern "
            self.textSubiecteInteres.set(subiecte)
            anyItem = True
        if self.Item5.get() == True:
            subiecte = subiecte + " Mixt "
            self.textSubiecteInteres.set(subiecte)
            anyItem = True


root = tk.Tk()
root.title("GUIFactOfTheDay")
app = Application(master = root)
root.mainloop()