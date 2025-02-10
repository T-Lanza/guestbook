from get_date import get_date
import json
import tkinter as tk

# Import Guestlist 
PATH = "DATA/guestlist.json"

with open(PATH, 'r') as file:
    guestlist = json.load(file)

def clear_screen(frame):
    frame.destroy()

def add_guest(name, email, guestlist):
    name_e = name.get()
    email_e = email.get()

    new_add = {
        "date": get_date(),
        "name": name_e,
        "email": email_e
    }
    
    guestlist.append(new_add)

    with open(PATH, 'w') as file:
        json.dump(guestlist, file, indent=4)

    name.delete(0, tk.END)
    email.delete(0, tk.END)

    signed_in_frame = tk.Frame(root)
    signed_in_frame.config(width=300, height=250)
    signed_in_frame.pack()

    label = tk.Label(signed_in_frame, text="Signed in!")
    label.config(font=("Helvetica", 14))
    label.place(x=100, y=100)

    button = tk.Button(signed_in_frame, text="Ok!")
    button.config(command=lambda: clear_screen(signed_in_frame))
    button.place(x=100, y=125)

# Build Base GUI
root = tk.Tk()
root.geometry("300x250")
root.config(bg="#E6EDFF")
root.title("Baby Shower Sign-in")

welcome = tk.Label(text="Welcome!")
welcome.config(font=("Helvetica", 24), bg="#E6EDFF")
welcome.place(x=75, y=25)

name_label = tk.Label(text="Name: ")
name_label.config(font=("Helvetica", 14), bg="#E6EDFF")
name_label.place(x=25, y=75)

name_entry = tk.Entry()
name_entry.config(width=30, bd=2, relief="sunken")
name_entry.place(x=25, y=95)

email_label = tk.Label(text="Email: ")
email_label.config(font=("Helvetica", 14), bg="#E6EDFF")
email_label.place(x=25, y=135)

email_entry = tk.Entry()
email_entry.config(width=30, bd=2, relief="sunken")
email_entry.place(x=25, y=155)

# Sign in Button
button = tk.Button(text="Sign In!")
button.config(command=lambda: add_guest(name_entry, email_entry, guestlist))
button.config(bg="#E6EDFF", bd=4)
button.place(x=105, y=195)

# Main Loop
root.mainloop()

