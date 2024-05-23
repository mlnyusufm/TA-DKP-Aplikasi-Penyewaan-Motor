import customtkinter as ctk
from MainFrame import MainFrame
from BorrowMotorFrame import BorrowMotorFrame
from ReturnMotorFrame import ReturnMotorFrame
from StockFrame import StockFrame
from HistoryFrame import HistoryFrame

class MotorRentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Penyewaan Motor")
        self.geometry("393x652")

        self.stockMotor = {
            "Honda": {
                "Beat": {"B1234ABC": 2, "B5678DEF": 3},
                "Vario": {"B9101GHI": 1, "B1121JKL": 2}
            },
            "Yamaha": {
                "NMAX": {"B3141MNO": 1, "B5161PQR": 2},
                "Aerox": {"B7181STU": 2, "B9202VWX": 1}
            },
            "Suzuki": {
                "Nex II": {"B1023YZA": 2, "B4053BCD": 2},
                "Address": {"B7083EFG": 1, "B9013HIJ": 3}
            }
        }
        self.borrowingHistory = []

        self.mainFrame = MainFrame(self)
        self.mainFrame.pack(fill="both", expand=True)

        self.borrowMotorFrame = BorrowMotorFrame(self)
        self.returnMotorFrame = ReturnMotorFrame(self)
        self.stockMotorFrame = StockFrame(self)
        self.historyFrame = HistoryFrame(self)

        self.showMainFrame()
        self.mainFrame.updateWelcomeLabel()

    def showMainFrame(self):
        self.borrowMotorFrame.pack_forget()
        self.returnMotorFrame.pack_forget()
        self.stockMotorFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.mainFrame.pack(fill="both", expand=True)

    def showBorrowMotorFrame(self):
        self.mainFrame.pack_forget()
        self.returnMotorFrame.pack_forget()
        self.stockMotorFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.borrowMotorFrame.pack(fill="both", expand=True)

    def showReturnMotorFrame(self):
        self.mainFrame.pack_forget()
        self.borrowMotorFrame.pack_forget()
        self.stockMotorFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.returnMotorFrame.pack(fill="both", expand=True)

    def showStockMotorFrame(self):
        self.mainFrame.pack_forget()
        self.borrowMotorFrame.pack_forget()
        self.returnMotorFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.stockMotorFrame.pack(fill="both", expand=True)
        self.stockMotorFrame.updateStock()

    def showHistoryFrame(self):
        self.mainFrame.pack_forget()
        self.borrowMotorFrame.pack_forget()
        self.returnMotorFrame.pack_forget()
        self.stockMotorFrame.pack_forget()
        self.historyFrame.pack(fill="both", expand=True)
        self.historyFrame.updateHistory()

if __name__ == "__main__":
    app = MotorRentalApp()
    app.mainloop()
