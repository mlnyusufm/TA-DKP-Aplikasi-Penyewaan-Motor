import customtkinter as ctk
from Page import Page
from datetime import datetime

class MainFrame(Page):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.labelWelcome = ctk.CTkLabel(self, text="Selamat Datang!", font=("Arial Bold", 24))
        self.labelWelcome.pack(pady=20)

        self.labelBorrowMotor = ctk.CTkButton(self, text="Pinjam Motor", command=self.master.showBorrowMotorFrame)
        self.labelBorrowMotor.pack(pady=10)

        self.labelReturnMotor = ctk.CTkButton(self, text="Kembalikan Motor", command=self.master.showReturnMotorFrame)
        self.labelReturnMotor.pack(pady=10)

        self.buttonStockMotor = ctk.CTkButton(self, text="Stok Motor", command=self.master.showStockMotorFrame)
        self.buttonStockMotor.pack(pady=10)

        self.buttonHistory = ctk.CTkButton(self, text="Riwayat Peminjaman", command=self.master.showHistoryFrame)
        self.buttonHistory.pack(pady=10)

        self.buttonExit = ctk.CTkButton(self, text="Keluar", command=self.master.quit)
        self.buttonExit.pack(pady=10)

    def updateWelcomeLabel(self):
        currentHour = datetime.now().hour
        if currentHour < 12:
            greeting = "Selamat Pagi!"
        elif 12 <= currentHour < 18:
            greeting = "Selamat Siang!"
        else:
            greeting = "Selamat Malam!"

        self.labelWelcome.configure(text=greeting)
