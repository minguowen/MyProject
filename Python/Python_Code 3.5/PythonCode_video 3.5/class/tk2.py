from tkinter import *

root = Tk()

photo = PhotoImage(file="bg.gif")
theLabel = Label(root,
                 text="学Python\n到FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("微软雅黑", 20),
                 fg="blue"
                 )
theLabel.pack()

mainloop()
