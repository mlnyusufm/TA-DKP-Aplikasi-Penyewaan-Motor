import customtkinter as ctk
from Page import Page
from tkinter import messagebox

class BorrowMotorFrame(Page):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.labelBorrowMotor = ctk.CTkLabel(self, text="Tambah List Peminjaman Motor", font=("Arial Bold", 20))
        self.labelBorrowMotor.pack(pady=10)

        self.labelMotorBrand = ctk.CTkLabel(self, text="Merk Motor:")
        self.labelMotorBrand.pack()
        self.selectedBrand = ctk.StringVar(self)
        self.selectedBrand.set("Pilih Merk")
        self.dropdownBrand = ctk.CTkComboBox(self, variable=self.selectedBrand, values=list(self.master.stockMotor.keys()), command=self.updateModelDropdown)
        self.dropdownBrand.pack(pady=10, padx=10)

        self.labelMotorModel = ctk.CTkLabel(self, text="Model Motor:")
        self.labelMotorModel.pack()
        self.selectedModel = ctk.StringVar(self)
        self.selectedModel.set("Pilih Model")
        self.dropdownModel = ctk.CTkComboBox(self, variable=self.selectedModel, values=["Pilih Model"], command=self.updatePlatDropdown)
        self.dropdownModel.pack(pady=10, padx=10)

        self.labelMotorPlat = ctk.CTkLabel(self, text="Nomor Plat Motor:")
        self.labelMotorPlat.pack()
        self.selectedPlat = ctk.StringVar(self)
        self.selectedPlat.set("Pilih Nomor Plat")
        self.dropdownPlat = ctk.CTkComboBox(self, variable=self.selectedPlat, values=["Pilih Nomor Plat"])
        self.dropdownPlat.pack(pady=10, padx=10)

        self.buttonAddBorrow = ctk.CTkButton(self, text="Tambah Peminjaman", command=self.addBorrow)
        self.buttonAddBorrow.pack(pady=10, padx=10)

        self.buttinBackToMain = ctk.CTkButton(self, text="Kembali", command=self.master.showMainFrame)
        self.buttinBackToMain.pack(pady=10, padx=10)

    def updateModelDropdown(self, *args):
        brand = self.selectedBrand.get()
        if brand != "Pilih Merk":
            models = list(self.master.stockMotor[brand].keys())
            self.selectedModel.set("Pilih Model")
            self.dropdownModel.configure(values=models)

    def updatePlatDropdown(self, *args):
        brand = self.selectedBrand.get()
        model = self.selectedModel.get()
        if model != "Pilih Model":
            plats = list(self.master.stockMotor[brand][model].keys())
            self.selectedPlat.set("Pilih Nomor Plat")
            self.dropdownPlat.configure(values=plats)

    def addBorrow(self):
        brand = self.selectedBrand.get()
        model = self.selectedModel.get()
        plat = self.selectedPlat.get()

        if brand == "Pilih Merk":
            messagebox.showerror("Error", "Silakan pilih merk motor.")
            return

        if model == "Pilih Model":
            messagebox.showerror("Error", "Silakan pilih model motor.")
            return

        if plat == "Pilih Nomor Plat":
            messagebox.showerror("Error", "Silakan pilih Nomor Plat motor.")
            return

        if self.master.stockMotor[brand][model][plat] <= 0:
            messagebox.showerror("Error", "Stok motor yang diminta tidak tersedia.")
            return

        self.master.stockMotor[brand][model][plat] -= 1
        self.master.borrowingHistory.append(("Peminjaman", brand, model, plat))

        messagebox.showinfo("Sukses", f"Peminjaman motor {brand} {model} Nomor Plat {plat} berhasil ditambahkan.")
        self.clearFields()

    def clearFields(self):
        self.selectedBrand.set("Pilih Merk")
        self.selectedModel.set("Pilih Model")
        self.selectedPlat.set("Pilih Nomor Plat")
        self.dropdownModel.configure(values=["Pilih Model"])
        self.dropdownPlat.configure(values=["Pilih Nomor Plat"])
