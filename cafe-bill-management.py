import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

menu = {
    'Pizza': 350,
    'Pasta': 230,
    'Sandwich': 280,
    'Burger': 200,
    'Cold Coffee': 160,
    'Cheesecake' : 300,
    'Cheesy Fries' : 190,
    'Momos' : 160,
    'Tacos': 290,
}

def generate_receipt_no():
    return f"RCPT{random.randint(1000, 9999)}"

def generate_bill():
    customer = customer_name_entry.get().strip()
    if not customer:
        messagebox.showwarning("Input Error", "Please enter the customer name.")
        return

    receipt_no = generate_receipt_no()
    bill_text.delete('1.0', tk.END)
    total = 0
    date_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    # Bill Header
    bill_text.insert(tk.END, "----- The Big Chill Café Bill -----\n")
    bill_text.insert(tk.END, f"Date/Time: {date_time}\n")
    bill_text.insert(tk.END, f"Customer Name: {customer}\n")
    bill_text.insert(tk.END, f"Receipt No: {receipt_no}\n\n")
    bill_text.insert(tk.END, f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total'}\n")
    bill_text.insert(tk.END, "-"*45 + "\n")
    
    # Order Details
    for item, entry in qty_entries.items():
        try:
            qty = int(entry.get())
            if qty > 0:
                price = menu[item]
                item_total = qty * price
                total += item_total
                bill_text.insert(tk.END, f"{item:<15}{qty:<10}{price:<10}{item_total}\n")
        except ValueError:
            continue

    # Totals
    gst = total * 0.05
    grand_total = total + gst
    bill_text.insert(tk.END, "\nSubtotal: ₹{:.2f}".format(total))
    bill_text.insert(tk.END, "\nGST (5%): ₹{:.2f}".format(gst))
    bill_text.insert(tk.END, "\nTotal Amount: ₹{:.2f}".format(grand_total))
    bill_text.insert(tk.END, "\n\nThank you for visiting!")

# GUI Setup
root = tk.Tk()
root.title("The Big Chill Café Billing System")

# Title
tk.Label(root, text="Welcome to The Big Chill Café ☕", font=("Arial", 16)).pack(pady=10)

# Customer Info Frame
customer_frame = tk.Frame(root)
customer_frame.pack(pady=5)

tk.Label(customer_frame, text="Customer Name:").pack(side='left')
customer_name_entry = tk.Entry(customer_frame)
customer_name_entry.pack(side='left')

# Menu Frame
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

qty_entries = {}
for item, price in menu.items():
    row = tk.Frame(menu_frame)
    row.pack(fill="x", padx=10, pady=2)
    tk.Label(row, text=f"{item} (₹{price})", width=20, anchor='w').pack(side='left')
    entry = tk.Entry(row, width=5)
    entry.pack(side='left')
    qty_entries[item] = entry

# Button
tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)

# Bill Output Text Area
bill_text = tk.Text(root, height=20, width=50)
bill_text.pack(pady=10)

root.mainloop()