from tkinter import *

class pyRemoteNG:
    def __init__(self,app):
        self.testbutton = ttk.Button(text="Test Button")
        self.testbutton.pack()

def main():
    root=Tk()
    root.title("pyRemoteNG")
    obj = pyRemoteNG(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 