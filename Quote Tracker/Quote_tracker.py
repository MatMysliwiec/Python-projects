import yfinance as yf
import time
import tkinter as tk
from tkinter import ttk


class StockTracker:
    def __init__(self, master, symbols, interval):
        self.master = master
        self.master.title("Stock Quote Tracker")
        self.symbols = symbols
        self.interval = interval

        self.tree = ttk.Treeview(self.master, columns=("Symbol", "Price", "Change"), show="headings")
        self.tree.heading("Symbol", text="Symbol")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Change", text="Change")
        self.tree.pack()

        self.update_stocks()

    def fetch_stock_data(self, symbol):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        current_price = data["Close"].iloc[-1]
        previous_price = data["Close"].iloc[-2]
        change = current_price - previous_price

        return current_price, change

    def update_stocks(self):
        for symbol in self.symbols:
            current_price, change = self.fetch_stock_data(symbol)
            change_direction = "🔼" if change >= 0 else "🔽"

            item_id = f"{symbol}_{current_price}"
            values = (symbol, f"${current_price:.2f}", f"{change_direction} ${abs(change):.2f)}")

            item_exists = False
            for child_item_id in self.tree.get_children():
                if child_item_id.startswith(symbol):
                    self.tree.item(child_item_id, values=values)
                    item_exists = True
                    break

            if not item_exists:
                self.tree.insert("", "end", iid=item_id, values=values)
        self.master.after(self.interval, self.update_stocks)


if __name__ == "__main__":
    root = tk.Tk()
    symbols = ["AAPL", "GOOGL", "MSFT"]
    interval = 600
    app = StockTracker(root, symbols, interval)
    root.mainloop()
