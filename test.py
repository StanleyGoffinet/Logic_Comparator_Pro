
import tkinter as tk

result = ""


def validate():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

        global result

        if todo.logic1.get() is None or todo.logic2.get() is None:
            result = "ko"
        else:
            result = "ok"
            logic3.set(str(todo.logic1.get()) + str(todo.logic2.get()))
        logic3.set(result)

        #equation.set(total)

        # initialze the result variable
        # by empty string

class Todo(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Logic Comparator Pro")
        self.geometry("800x400")

        self.logic1 = tk.StringVar()
        self.logic2 = tk.StringVar()

        self.name_label1 = tk.Label(self, text="Logic Proposition 1", pady=10, bg="light grey", relief='raised').pack(fill=tk.BOTH)
        self.logic_entry1 = tk.Entry(self, bg="white", fg="black", textvariable=self.logic1).pack(fill=tk.BOTH)
        self.name_label2 = tk.Label(self, text="Logic Proposition 2", pady=10, bg="light grey", relief='raised').pack(fill=tk.BOTH)
        self.logic_entry2 = tk.Entry(self, bg="white", fg="black", textvariable=self.logic2).pack(fill=tk.BOTH)

        self.logic1.set('enter your first logic expression')
        self.logic2.set('enter your second logic expression')


if __name__ == "__main__":

    todo = Todo()
    todo.configure(background="light blue")
    logic3 = tk.StringVar()
    bouton_validate = tk.Button(todo, text=' validate ', fg='white', bg='blue', bd=4, command=validate).pack(fill=tk.BOTH, padx=350, pady=5)
    logic_entry3 = tk.Entry(bg="white", fg="black", textvariable=logic3).pack(fill=tk.BOTH, padx=350)
    todo.mainloop()
