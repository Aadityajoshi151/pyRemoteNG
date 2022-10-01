from tkinter import *

class pyRemoteNG:
    def __init__(self,app):
        left_panel = Frame(app, bg='blue', width=300, height=app.winfo_screenheight())
        left_panel.grid(row=1, column=0, sticky="ns")
        left_panel.grid_propagate(False) 
        terminal = Frame(app, bg='yellow', width=app.winfo_screenwidth(), height=app.winfo_screenheight(), padx=3, pady=3)
        terminal.grid(row=1, column=1, sticky="nsew")

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
 