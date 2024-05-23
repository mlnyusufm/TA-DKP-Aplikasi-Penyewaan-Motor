import customtkinter as ctk
from Page import Page

class StockFrame(Page):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.labelTitle = ctk.CTkLabel(self, text="Stok Motor", font=("Arial Bold", 24))
        self.labelTitle.pack(pady=20)

        self.frameStock = ctk.CTkScrollableFrame(self)
        self.frameStock.pack(pady=10, padx=10, fill="both", expand=True)
        self.updateStock()

        self.buttonBack = ctk.CTkButton(self, text="Kembali", command=self.master.showMainFrame)
        self.buttonBack.pack(pady=10)

    def updateStock(self):
        for widget in self.frameStock.winfo_children():
            widget.destroy()

        for brand, models in self.master.stockMotor.items():
            for model, plats in models.items():
                for plat, quantity in plats.items():
                    card = ctk.CTkFrame(self.frameStock)
                    card.pack(pady=10, padx=10, side="top", expand=True, fill="both")

                    labelBrand = ctk.CTkLabel(card, text=f"{brand}", font=("Arial Bold", 12))
                    labelBrand.pack(pady=(10, 4))

                    labelModel = ctk.CTkLabel(card, text=f"{model}", font=("Arial", 10))
                    labelModel.pack()

                    labelPlat = ctk.CTkLabel(card, text=f"Nomor Plat: {plat}", font=("Arial", 10))
                    labelPlat.pack()

                    label_quantity = ctk.CTkLabel(card, text=f"Stok: {quantity}", font=("Arial", 10))
                    label_quantity.pack(pady=(2, 5))

