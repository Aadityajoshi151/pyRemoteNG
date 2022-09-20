from tkinter import *

class pyRemoteNG:
    def __init__(self,app):
        self.testbutton = Button(text="Test Button")
        self.testbutton.pack()

def main():
    root=Tk()
    root.title("pyRemoteNG")
    mymenu = Menu(root)
    root.config(menu=mymenu)
    myfilemenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="File", menu=myfilemenu)
    myfilemenu.add_command(label="New connection")
    myfilemenu.add_command(label="Export to file")
    myfilemenu.add_command(label="SSH File transfer")
    myfilemenu.add_separator()
    myfilemenu.add_command(label="Quit", command=lambda: root.quit())
    obj = pyRemoteNG(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 