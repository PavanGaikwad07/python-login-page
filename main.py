import tkinter as tk
from tkinter import messagebox

# Hardcoded login credentials
USERNAME = "admin"
PASSWORD = "1234"

# Function to check login
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hides password
password_entry.pack(pady=5)

# Login button
tk.Button(root, text="Login", command=check_login).pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
