import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.master.geometry("500x500")
        self.master.configure(bg="black")
        
        self.balance = 10000  # Default balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []
        
        self.enter_pin_screen()
    
    def enter_pin_screen(self):
        self.clear_window()
        tk.Label(self.master, text="Welcome to ATM", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=10)
        tk.Label(self.master, text="Enter PIN", font=("Arial", 16, "bold"), bg="black", fg="white").pack(pady=10)
        self.pin_entry = tk.Entry(self.master, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=5)
        tk.Button(self.master, text="Submit", command=self.validate_pin, font=("Arial", 14), bg="gray", fg="white").pack(pady=5)
    
    def validate_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.create_widgets()
        else:
            messagebox.showerror("Error", "Invalid PIN! Try again.")
    
    def create_widgets(self):
        self.clear_window()
        tk.Label(self.master, text="ATM Machine", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=10)
        
        button_frame = tk.Frame(self.master, bg="black")
        button_frame.pack(pady=20)
        
        buttons = [
            ("Balance Inquiry", self.check_balance),
            ("Cash Withdrawal", self.withdraw_cash),
            ("Cash Deposit", self.deposit_cash),
            ("Change PIN", self.change_pin),
            ("Transaction History", self.view_transaction_history),
            ("Exit", self.master.destroy)
        ]
        
        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command, font=("Arial", 14), bg="gray", fg="white", width=20).pack(pady=5)
    
    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append("Checked Balance")
    
    def withdraw_cash(self):
        amount = self.get_amount("Withdraw Amount")
        if amount and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} withdrawn successfully!\nUpdated Balance: ₹{self.balance}")
        elif amount:
            messagebox.showerror("Error", "Insufficient balance!")
    
    def deposit_cash(self):
        amount = self.get_amount("Deposit Amount")
        if amount:
            self.balance += amount
            self.transaction_history.append(f"Deposited ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} deposited successfully!\nUpdated Balance: ₹{self.balance}")
    
    def change_pin(self):
        new_pin = self.get_input("Enter New PIN")
        if new_pin and len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            self.transaction_history.append("Changed PIN")
            messagebox.showinfo("Success", "PIN changed successfully!")
        else:
            messagebox.showerror("Error", "Invalid PIN! Must be 4 digits.")
    
    def view_transaction_history(self):
        history = "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."
        messagebox.showinfo("Transaction History", history)
    
    def get_amount(self, title):
        amount = self.get_input(title)
        if amount and amount.isdigit():
            return int(amount)
        messagebox.showerror("Error", "Invalid amount!")
        return None
    
    def get_input(self, prompt):
        input_window = tk.Toplevel(self.master)
        input_window.title(prompt)
        input_window.geometry("300x150")
        
        tk.Label(input_window, text=prompt, font=("Arial", 12)).pack(pady=10)
        entry = tk.Entry(input_window, font=("Arial", 12))
        entry.pack(pady=5)
        
        def submit():
            self.input_value = entry.get()
            input_window.destroy()
        
        self.input_value = None
        tk.Button(input_window, text="Submit", command=submit, font=("Arial", 12), bg="gray", fg="white").pack(pady=5)
        input_window.wait_window()
        return self.input_value
    
    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
