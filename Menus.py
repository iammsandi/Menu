# menus  
import tkinter as tk 

from  tkinter import messagebox 

def open_file():
    messagebox.showinfo("Open File", "Open file dialog would appear here.")
    
def exit_app():
    root.quit()

root=tk.Tk()
root.title("Menu Example")
root.geometry("600x400")
menu_bar = tk.Menu(root)
 
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
 
root.config(menu=menu_bar)
 
root.mainloop()