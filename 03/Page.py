import customtkinter as ctk

class Page(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

    def show(self):
        self.pack(fill="both", expand=True)

    def hide(self):
        self.pack_forget()
