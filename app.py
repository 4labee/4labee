import tkinter as tk
import ttkbootstrap as ttk

# Create tkinter class object for app 
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        
        x = int(self.winfo_screenwidth()/2)
        y = int(self.winfo_screenheight()/1.5)
        
        self.title("To Do")
        self.minsize(x, y)
        # self.resizable(False, False)
        self.add_task_frame  = AddTaskFrame(self)
        self.task_frame = ViewTaskFrame(self)
        self.done_task_frame = DoneTaskFrame(self)

class AddTaskFrame(ttk.Frame):
    def __init__(self, window):
        super().__init__()

        self.place(x=0, y=0, relwidth=1, relheight=0.3) 
        ttk.Label(self, background='black').pack(expand=True, fill='both')

class ViewTaskFrame(ttk.Frame):
    def __init__(self, window):
        super().__init__()
        
        self.place(x=0, rely=0.3, relwidth=1, relheight=0.3) 
        ttk.Label(self, background='grey').pack(expand=True, fill='both')

class DoneTaskFrame(ttk.Frame):
    def __init__(self, window):
        super().__init__()
        
        self.place(x=0, rely=0.6, relwidth=1, relheight=0.4) 
        ttk.Label(self, background='green').pack(expand=True, fill='both')

if __name__ == "__main__":
    app = App()
    app.mainloop()