import tkinter as tk
from tkinter import ttk, messagebox


class PaymentForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MobileOperator: Приём платежей")
        self.geometry("600x450")
        self.subscribers = {
            "Иванов И.И. (ЛС 1001)": 150.0,
            "Петров П.П. (ЛС 1002)": 0.0,
            "Сидоров С.С. (ЛС 1003)": 320.5,
        }
        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text="Абонент:").place(x=20, y=20)
        self.cmb_subscriber = ttk.Combobox(self, width=30, values=list(self.subscribers.keys()))
        self.cmb_subscriber.current(0)
        self.cmb_subscriber.place(x=150, y=18)

        tk.Label(self, text="Сумма платежа:").place(x=20, y=60)
        self.txt_amount = tk.Entry(self, width=32)
        self.txt_amount.place(x=150, y=58)

        tk.Label(self, text="Способ оплаты:").place(x=20, y=100)
        self.cmb_method = ttk.Combobox(self, width=30, values=["Карта", "Наличные", "Онлайн"])
        self.cmb_method.current(0)
        self.cmb_method.place(x=150, y=98)

        self.btn_create = tk.Button(self, text="Принять платёж", width=25, height=2,
                                    command=self.on_accept_payment)
        self.btn_create.place(x=150, y=140)

        self.tree = ttk.Treeview(self, columns=("sub", "amount", "method", "balance"),
                                 show="headings", height=8)
        for col, title in zip(("sub", "amount", "method", "balance"),
                              ("Абонент", "Сумма", "Способ", "Баланс")):
            self.tree.heading(col, text=title)
            self.tree.column(col, width=120)
        self.tree.place(x=20, y=190)

    def on_accept_payment(self):
        subscriber = self.cmb_subscriber.get()
        amount_text = self.txt_amount.get()
        method = self.cmb_method.get()

        amount = float(amount_text) if amount_text else 0.0

        self.subscribers[subscriber] += amount
        new_balance = self.subscribers[subscriber]

        self.tree.insert("", "end", values=(subscriber, amount, method, f"{new_balance:.2f}"))
        self.txt_amount.delete(0, tk.END)

        messagebox.showinfo("Внимание", "Платёж успешно принят!",
                            icon=messagebox.ERROR)  

if __name__ == "__main__":
    PaymentForm().mainloop()
