
from tkinter import *
import string

result = ""
normal_form_1 = ""
normal_form_2 = ""
alphabet = list(string.ascii_letters)
symbol_lexique = ["(",")"," ","&","|","-"]
all_symbol = symbol_lexique + alphabet

def check():
    global normal_form_1
    global normal_form_2
    normal_form_1 = str(logic1.get())
    normal_form_2 = str(logic2.get())
    list1 = list(normal_form_1)
    list2 = list(normal_form_2)

    count_variable1 = 0
    count_variable2 = 0

    for letter in alphabet:
        if normal_form_1.count(letter) > 0:
            count_variable1 += 1
        if normal_form_2.count(letter) > 0:
            count_variable2 += 1
    logic1.set(str(count_variable1))
    logic2.set(str(count_variable2))
    if count_variable1 != count_variable2:
        logic1.set("bad Entry, different number of variable, the first one has " + str(count_variable1) + " variables")
        logic2.set("bad Entry, different number of variable, the second one has " + str(count_variable2) + " variables")
    else:
        for symbol in list1:
            if symbol not in all_symbol:
                logic1.set("bad Entry, unresolved symbol : " + symbol)
        for symbol in list2:
            if symbol not in all_symbol:
                logic2.set("bad Entry, unresolved symbol : " + symbol)


if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Logic Comparator Pro")
    gui.geometry("800x400")

    logic1 = StringVar()
    logic2 = StringVar()
    logicResult = StringVar()

    name_label1 = Label(gui, text="Logic Proposition 1", pady=10, bg="light grey", relief='raised').pack(fill=X)
    logic_entry1 = Entry(gui, bg="white", fg="black", textvariable=logic1).pack(fill=BOTH)
    name_label2 = Label(gui, text="Logic Proposition 2", pady=10, bg="light grey", relief='raised').pack(fill=BOTH)
    logic_entry2 = Entry(gui, bg="white", fg="black", textvariable=logic2).pack(fill=BOTH)
    bouton_check = Button(gui, text=' Check ', fg='white', bg='blue', bd=4, command=lambda: check()).pack(fill=BOTH, padx=350, pady=5)
    bouton_compare = Button(gui, text=' Compare ', fg='white', bg='green', bd=4, command=lambda: check()).pack(fill=BOTH, padx=350, pady=5)

    logic_entry3 = Entry(gui, bg="white", fg="black", textvariable=logicResult).pack(fill=BOTH, padx=350)
    logic1.set('enter your first logic expression')
    logic2.set('enter your second logic expression')
    logic1.set('(a | b) & (b | a | d) ')
    logic2.set('(b | c) & a')

    gui.mainloop()


