import customtkinter
import tkinter

windows = tkinter.Tk()
windows.title("Pokemon")
windows.geometry("380x300")
windows.config(background="gray36")
label = tkinter.Label(windows, text="Pokemon Game", bg="gray37", fg="grey94")
label.pack(fill=tkinter.X, ipady="10")

for i in range(100):
    label.pack(pady=i)

windows.mainloop()