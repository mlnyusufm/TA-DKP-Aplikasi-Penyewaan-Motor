import customtkinter as ctk
from Page import Page

class HistoryFrame(Page):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.labelTitle = ctk.CTkLabel(self, text="Riwayat Peminjaman", font=("Arial Bold", 24))
        self.labelTitle.pack(pady=20)

        self.frameHistory = ctk.CTkScrollableFrame(self)
        self.frameHistory.pack(pady=10, padx=10, fill="both", expand=True)
        self.updateHistory()

        self.buttonBack = ctk.CTkButton(self, text="Kembali", command=self.master.showMainFrame)
        self.buttonBack.pack(pady=10)

    def updateHistory(self):
        for widget in self.frameHistory.winfo_children():
            widget.destroy()

        for entry in self.master.borrowingHistory:
            type_, brand, model, plat = entry  # Ekstraksi informasi dari entri
            card = ctk.CTkFrame(self.frameHistory)
            card.pack(pady=10, padx=10, side="top", expand=True, fill="both")

            labelEntry = ctk.CTkLabel(card, text=f"{type_}: {brand} {model} - {plat}", font=("Arial", 10))
            labelEntry.pack(pady=5)
