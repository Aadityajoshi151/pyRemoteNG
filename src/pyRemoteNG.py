from tkinter import *

class pyRemoteNG:
    def __init__(self,app):
        left_frame = Frame(app, width=300, height=app.winfo_screenheight(), bg="cyan")
        left_frame.grid(row=0, column=0)
        left_frame.grid_propagate(False) 
        terminal_frame = Frame(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight(), bg="green")
        terminal_frame.grid(row=0, column=1)
        connections = Listbox(left_frame, height=30, width=42, relief=)
        connections.grid(row=0, column=0)
        connections.insert(1, "Test")

def main():
    root=Tk()
    root.title("pyRemoteNG")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    mymenu = Menu(root)
    root.config(menu=mymenu)
    myfilemenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="File", menu=myfilemenu)
    myfilemenu.add_command(label="Add New connection")
    myfilemenu.add_command(label="Quick Connect")
    myfilemenu.add_command(label="Export to file")
    myfilemenu.add_command(label="SSH File transfer")
    myfilemenu.add_separator()
    myfilemenu.add_command(label="Quit", command=lambda: root.quit())
    
    obj = pyRemoteNG(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 