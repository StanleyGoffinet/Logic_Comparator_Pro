
from tkinter import *

result = ""
normal_form_1 = ""
normal_form_2 = ""




if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Logic Comparator Pro")
    gui.geometry("800x400")

    logic1 = StringVar()
    logic2 = StringVar()
    logicResult = StringVar()

    name_label1 = Label(gui, text="Logic Proposition 1", pady=10, bg="light grey", relief='raised').pack(fill=BOTH)
    logic_entry1 = Entry(gui, bg="white", fg="black", textvariable=logic1).pack(fill=BOTH)
    name_label2 = Label(gui, text="Logic Proposition 2", pady=10, bg="light grey", relief='raised').pack(fill=BOTH)
    logic_entry2 = Entry(gui, bg="white", fg="black", textvariable=logic2).pack(fill=BOTH)
    bouton_check = Button(gui, text=' Check ', fg='white', bg='blue', bd=4, command=check()).pack(fill=BOTH, padx=350, pady=5)
    bouton_compare = Button(gui, text=' Compare ', fg='white', bg='green', bd=4, command=compare()).pack(fill=BOTH, padx=350, pady=5)

    logic_entry3 = Entry(gui, bg="white", fg="black", textvariable=logicResult).pack(fill=BOTH, padx=350)

    logic1.set('enter your first logic expression')
    logic2.set('enter your second logic expression')

    gui.mainloop()


