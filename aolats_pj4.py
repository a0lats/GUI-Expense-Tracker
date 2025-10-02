# Author: Adeoluwa (Ade) Olateru-Olagbegi
# Project: GUI Expense Tracker
# Date: 08/12/2025
# Description: Desktop GUI app for logging expenses and visualizing spending 
# with charts using Tkinter + Matplotlib.

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

expenses = []

def add_expense(amount, category):
    expenses.append({"amount": float(amount), "category": category})

def show_expenses():
    return expenses

def plot_expenses():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to plot")
        return
    
    categories = [e["category"] for e in expenses]
    amounts = [e["amount"] for e in expenses]

    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.title("Expense Tracker")
    plt.show()


# -------------------------
# Test Calls (Safe Version)
# -------------------------
if not expenses:  # Only add demo data once
    add_expense(120, "Food")
    add_expense(60, "Transport")
    add_expense(200, "Rent")
    add_expense(45, "Entertainment")

print("Expenses:", show_expenses())
plot_expenses()