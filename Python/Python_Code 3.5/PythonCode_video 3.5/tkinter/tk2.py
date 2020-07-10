import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.hi_there = tk.Button(frame, text = '打招呼', bg = 'blue', fg = 'white', command = self.say_hello)
        self.hi_there.pack()
        
    def say_hello(self):
        print("hello,everyone!")
        
root = tk.Tk()
app = APP(root)

root.mainloop()
