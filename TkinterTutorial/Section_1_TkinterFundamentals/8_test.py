import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

example_test_2 = tk.Tk()
example_test_2.geometry("300x200+600+0")
example_test_2.resizable(False,False)
example_test_2.title('Demo_2')

def download_clicked():
    showinfo(
        title="Information",
        message="Download button clicked!"
    )

download_icon = tk.PhotoImage(file="D:/download.png")
download_button = ttk.Button(
    example_test_2,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

example_test_2.mainloop()