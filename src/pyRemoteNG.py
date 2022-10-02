from tkinter import *
import sqlite3

class pyRemoteNG:
    def run_db_query(self, query):
        try:
            connection_obj = sqlite3.connect("connections.db")
            cursor = connection_obj.cursor()
            obj = cursor.execute(query)
            connection_obj.commit()
            connection_obj.close()
            return obj
        except:
            pass

    def __init__(self, app):
        #Initialise Database
        query_response = self.run_db_query("""CREATE TABLE connections(
            connection_name text,
            hostname text,
            usernmae text,
            password text
            )
        """)
        left_frame = Frame(app, width=300, height=app.winfo_screenheight(), bg="cyan")
        left_frame.grid(row=0, column=0)
        left_frame.grid_propagate(False) 
        terminal_frame = Frame(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight(), bg="green")
        terminal_frame.grid(row=0, column=1)
        connections = Listbox(left_frame, height=30, width=42)
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
 