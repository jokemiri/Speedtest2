from tkinter import *
import speedtest
import tkinter as tk

root=tk.Tk()
root.geometry("360x600")
root.resizable(False, False)
root.title("Speedtest by Josh")
root.configure(background='#d0dbe4')

#window icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#button
start=PhotoImage(file='start.png')
Button(root, image = start, bg='#d0dbe4', bd=0, activebackground='#d0dbe4').place(x=110, y=420)

#window images
download=tk.PhotoImage(file="download.png")
upload=tk.PhotoImage(file="upload.png")
ping=tk.PhotoImage(file="ping.png")

main=PhotoImage(file='main.png')



#place images
Label(root, image=download, bg='#d0dbe4').place(x=30, y=15)
Label(root, image=upload, bg='#d0dbe4').place(x=150, y=15)
Label(root, image=ping, bg='#d0dbe4').place(x=270, y=15)

Label(root, image=main, bg='#d0dbe4').place(x=50, y=150)



root.mainloop()