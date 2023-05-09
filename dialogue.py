from tkinter import *
from tkinter import ttk
root = Tk()

ttk.Entry(root).grid()
def dismiss ():
    dlg.grab_release()
    dlg.destroy()

dlg = Toplevel(root)
ttk.Button(dlg, text="Done", command=dismiss).grid()
dlg.protocol("WM_DELETE_WINDOW", dismiss)
dlg.transient(root)
dlg.wait_visibility()
dlg.grab_set()
dlg.wait_window()

root.mainloop()


