import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# ExpenseTracker: GUI app for recording, filtering, and summarizing expenses.
# Uses dictionary for each expense, list for collection, JSON for file storage.
# Demonstrates dynamic typing, datetime library, and exception handling.
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker - Python")
        self.root.geometry("800x500")
        
        # Storage for expenses (Python dictionary)
        self.expenses = []
        self.load_data()
        
        # Create GUI
        self.create_widgets()
        self.refresh_list()
    
    def create_widgets(self):
        # Input Frame (Top)
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # Date
        tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5)
        self.date_entry = tk.Entry(input_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        # Amount
        tk.Label(input_frame, text="Amount:").grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=0, column=3, padx=5)
        
        # Category
        tk.Label(input_frame, text="Category:").grid(row=0, column=4, padx=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(input_frame, textvariable=self.category_var, 
                                           values=["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"], 
                                           width=12)
        self.category_combo.grid(row=0, column=5, padx=5)
        self.category_combo.set("Food")
        
        # Description
        tk.Label(input_frame, text="Description:").grid(row=0, column=6, padx=5)
        self.desc_entry = tk.Entry(input_frame, width=20)
        self.desc_entry.grid(row=0, column=7, padx=5)
        
        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Add Expense", command=self.add_expense, bg="lightgreen", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_expense, bg="lightcoral", width=15).pack(side=tk.LEFT, padx=5)
        
        # Filter Frame
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=5)
        
        tk.Label(filter_frame, text="Filter by Category:").pack(side=tk.LEFT, padx=5)
        self.filter_var = tk.StringVar()
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, 
                                         values=["All", "Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"], 
                                         width=12)
        self.filter_combo.pack(side=tk.LEFT, padx=5)
        self.filter_combo.set("All")
        tk.Button(filter_frame, text="Apply Filter", command=self.refresh_list, bg="lightblue", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="Show All", command=self.show_all, width=12).pack(side=tk.LEFT, padx=5)
        
        # Expenses List (Treeview)
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(list_frame, columns=("Date", "Amount", "Category", "Description"), 
                                  show="headings", yscrollcommand=scrollbar.set)
        
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount ($)")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        
        self.tree.column("Date", width=100)
        self.tree.column("Amount", width=80)
        self.tree.column("Category", width=100)
        self.tree.column("Description", width=200)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Summary Frame (Bottom)
        summary_frame = tk.Frame(self.root)
        summary_frame.pack(pady=10)
        
        self.summary_label = tk.Label(summary_frame, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.summary_label.pack()
        
        self.category_summary_label = tk.Label(summary_frame, text="", font=("Arial", 10))
        self.category_summary_label.pack()
    
    def add_expense(self):
        # Get values
        date = self.date_entry.get()
        amount = self.amount_entry.get()
        category = self.category_var.get()
        description = self.desc_entry.get()
        
        # Validation
        if not amount:
            messagebox.showwarning("Warning", "Please enter an amount")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Warning", "Amount must be a number")
            return
        
        # Create expense dictionary (Python dictionary for data storage)
        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        
        self.expenses.append(expense)
        self.save_data()
        self.refresh_list()
        
        # Clear entries
        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", "Expense added successfully!")
    
    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an expense to delete")
            return
        
        # Get the index
        for item in selected:
            index = self.tree.index(item)
            del self.expenses[index]
        
        self.save_data()
        self.refresh_list()
        messagebox.showinfo("Success", "Expense deleted!")
    
    def refresh_list(self):
        # Clear current list
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Filter expenses
        filter_category = self.filter_var.get()
        filtered_expenses = self.expenses
        if filter_category != "All":
            filtered_expenses = [e for e in self.expenses if e["category"] == filter_category]
        
        # Add to list
        for expense in filtered_expenses:
            self.tree.insert("", tk.END, values=(
                expense["date"],
                f"${expense['amount']:.2f}",
                expense["category"],
                expense["description"]
            ))
        
        # Update summary
        self.update_summary(filtered_expenses)
    
    def show_all(self):
        self.filter_var.set("All")
        self.refresh_list()
    
    def update_summary(self, expenses_list):
        # Calculate total
        total = sum(e["amount"] for e in expenses_list)
        self.summary_label.config(text=f"Total Expenses: ${total:.2f}")
        
        # Calculate by category (dictionary for category totals)
        category_totals = {}
        for expense in expenses_list:
            cat = expense["category"]
            category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]
        
        # Display category summary
        summary_text = "By Category: "
        for cat, amount in category_totals.items():
            summary_text += f"{cat}: ${amount:.2f}  |  "
        
        self.category_summary_label.config(text=summary_text)
    
    def save_data(self):
        # Save to JSON file (Python's built-in JSON library)
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f, indent=2)
    
    def load_data(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()