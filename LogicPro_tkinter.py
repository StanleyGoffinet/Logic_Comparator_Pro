from tkinter import *
import string
import itertools

result = ""
normal_form_1 = ""
normal_form_2 = ""
list1 = []
list2 = []
alphabet = list(string.ascii_letters)
symbol_lexique = ['(', ')', ' ', '&', '|', '-', '¬', '∨', '∧']
all_symbol = symbol_lexique + alphabet
nb_variable = 0
count_variable1 = []
count_variable2 = []
truth_table_list = []
input_before1 = []
input_before2 = []
truth_table_list_historic = []


def before(nb):
    """
    This is the before function called by the check button
    The goal of this function is to change the input with
    the inputs gived before
    """
    global input_before1, input_before2

    if nb == 1 and len(input_before1) > 1:
        logic_entry1.delete('1.0', END)
        logic_entry1.insert('1.0', str(input_before1[-2]).strip('"[]\''))
        log1.set('')
        log_entry1.config(bg="white")
        input_before1.pop(-2)

    elif nb == 2 and len(input_before2) > 1:
        logic_entry2.delete('1.0', END)
        logic_entry2.insert('1.0', str(input_before2[-2]).strip('"[]\''))
        log2.set('')
        log_entry2.config(bg="white")
        input_before2.pop(-2)


def compare():
    """
    This is the check function called by the check button
    The goal of this function is to check if the 2 inputs (the 2 logical expressions)
    are valid syntaxicaly and lexicaly
    """
    global nb_variable, normal_form_1, normal_form_2, list1, list2, count_variable2, count_variable1, truth_table_list,\
        input_before1, input_before2

    logicResult.set("")
    log1.set("")
    log2.set("")

    count_variable1 = []
    count_variable2 = []
    count_bad_1 = []
    count_bad_2 = []

    logic1.set(logic_entry1.get(1.0, 'end-1c'))
    logic2.set(logic_entry2.get(1.0, 'end-1c'))
    normal_form_1_no_split = logic1.get()
    normal_form_2_no_split = logic2.get()

    normal_form_1 = "".join(normal_form_1_no_split.splitlines())
    normal_form_2 = "".join(normal_form_2_no_split.splitlines())

    #print(logic1.get(), normal_form_1)

    input_before1.append(logic1.get())
    input_before2.append(logic2.get())
    list1 = list(normal_form_1)
    list2 = list(normal_form_2)
    logic_entry3.config(bg="white")
    #print(input_before1, input_before2)
    for l in range(0, len(list1)):
            if list1[l] not in all_symbol:
                count_bad_1.append(list1[l])

    for l in range(0, len(list2)):
            if list2[l] not in all_symbol:
                count_bad_2.append(list2[l])

    for letter in alphabet:
            if normal_form_1.count(letter) > 0:
                count_variable1.append(str(letter))
            if normal_form_2.count(letter) > 0:
                count_variable2.append(str(letter))

    if len(count_bad_1) > 0:
            log1.set("Unresolved symbol: " + str(count_bad_1))
            log_entry1.config(bg="orange red")

    elif len(count_bad_2) > 0:
            log2.set("Unresolved symbol: " + str(count_bad_2))
            log_entry2.config(bg="orange red")

    elif len(count_variable1) != len(count_variable2):
            log1.set("Not same number of variables: " + str(len(count_variable1)))
            log_entry1.config(bg="DarkOrange")
            log2.set("Not same number of variables: " + str(len(count_variable2)))
            log_entry2.config(bg="DarkOrange")
            compare_variable_widow()

    elif len(count_variable1) != len(count_variable2) or len(set(count_variable1).intersection(set(count_variable2))) != len(count_variable1):
            log1.set("Not same variable: " + str(count_variable1))
            log_entry1.config(bg="DarkOrange")
            log2.set("Not same variable: " + str(count_variable2))
            log_entry2.config(bg="DarkOrange")
            compare_variable_widow()

    else:

            log_entry1.config(bg="pale green")
            log_entry2.config(bg="pale green")
            log1.set("OK")
            log2.set("OK")
            nb_variable = len(count_variable1)
            truth_table_list = []
            logic1.set(normal_form_1)
            logic2.set(normal_form_2)
            logic_table_instance = list(itertools.product('01', repeat=nb_variable))

            # print(logic_table_instance)

            normal_form_1_format = format_logic(normal_form_1)
            normal_form_2_format = format_logic(normal_form_2)

            for e in range(0, len(logic_table_instance)):
                normal_form_1_format_copy = normal_form_1_format
                normal_form_2_format_copy = normal_form_2_format
                for i in range(0, len(count_variable1)):
                    normal_form_1_format_copy = normal_form_1_format_copy.replace(count_variable1[i],
                                                                                  logic_table_instance[e][i])
                    normal_form_2_format_copy = normal_form_2_format_copy.replace(count_variable1[i],
                                                                                  logic_table_instance[e][i])

                normal_form_1_format_copy_final = normal_form_1_format_copy.replace("-0", "1").replace("-1", "0") \
                    .replace("- 0", "1").replace("- 1", "0").replace("&", " and ").replace("|", " or ").replace("-",
                                                                                                                " not ")
                normal_form_2_format_copy_final = normal_form_2_format_copy.replace("-0", "1").replace("-1", "0") \
                    .replace("- 0", "1").replace("- 1", "0").replace("&", " and ").replace("|", " or ").replace("-",
                                                                                                                " not ")

                try:
                    eval(normal_form_1_format_copy_final)
                except SyntaxError:
                    log1.set("Syntax Error")
                    log_entry1.config(bg="orange red")
                try:
                    eval(normal_form_2_format_copy_final)
                except SyntaxError:
                    log2.set("Syntax Error")
                    log_entry2.config(bg="orange red")

                truth_table_list.append((logic_table_instance[e], int(eval(normal_form_1_format_copy_final)),
                                         int(eval(normal_form_2_format_copy_final))))

                # print(normal_form_1_format_copy_final, normal_form_2_format_copy_final)
            # print(truth_table_list)
            # print(truth_table_list)
            logicResult.set("They're equal")
            logic_entry3.config(bg="LawnGreen")
            for test in range(0, len(truth_table_list)):
                if truth_table_list[test][1] != truth_table_list[test][2]:
                    logicResult.set("Not Equal")
                    logic_entry3.config(bg="orange red")
                    break
                else:
                    continue
            truth_table_list_historic.append(truth_table_list)
            true_table_canvas(truth_table_list)


def true_table_canvas(table):
    """
    This is the true_table_canvas called in the compare function
    if the comparaison was made and a result is gived
    :param table:
    """

    scrollbar.grid(row=4, column=4, rowspan=5, sticky=W + N + E + S)
    scrollbar.config(command=mylist.yview)

    mylist.insert(END, 'Here is the table of truth found with:')
    string_proposition = logic1.get() + " AND " + logic2.get()
    mylist.insert(END, string_proposition)
    start_table_string = ""
    for var in range(nb_variable):
        start_table_string = start_table_string + "          " + str(count_variable1[var])
    start_table_string += "          Logic_1_value          Logic_2_value"
    mylist.insert(END, start_table_string)

    for line in range(len(table)):
        table_string_value = ""
        for var in range(nb_variable):
            table_string_value = table_string_value + "          " + str(table[line][0][var])

        table_string_value += "                      " + str(table[line][1]) + "                                 " + str(table[line][2])
        mylist.insert(END, table_string_value)

    mylist.grid(row=4, column=0, columnspan=4, rowspan=2, sticky=W+N+E+S)


def format_logic(logic_string):
    """
    This is the format_logic function called in the function compare()
    The goal is to return the 2 inputs gived by the user(s)
    The return is different than the input
    where the caracter is not valid for a logic evaluation

    :param logic_string:
    :return: String
    """
    logic_string_copy = logic_string.replace("∧", "&").replace("∨", "|").replace("¬", "-")
    return logic_string_copy


def reset():
    """
    This is the reset function called by the reset button
    The goal of this function is to reset all the value calculate or implemented as empty
    or in the initial state of the application
    """
    global nb_variable, normal_form_1, normal_form_2, list1, list2, count_variable2, count_variable1,\
        truth_table_list, input_before1, input_before2, truth_table_list_historic
    logicResult.set("")
    log2.set("")
    log1.set("")
    normal_form_1 = ""
    normal_form_2 = ""
    list1 = []
    list2 = []
    count_variable1 = []
    count_variable2 = []
    truth_table_list = []
    nb_variable = 0
    log_entry1.config(bg="white")
    log_entry2.config(bg="white")
    logic_entry3.config(bg="white")
    input_before1 = []
    input_before2 = []
    truth_table_list_historic = []


def help_window():
    """
    function use for help the user to use Logic Comparator Pro
    """
    top = Toplevel(gui)
    lab = Label(top, text="User Guide :")
    lab.pack()
    lab2 = Label(top, text="The conjunction symbol is : '&' (key 1 on the keyboard) ")
    lab2.pack()
    lab3 = Label(top, text="The disjunction symbol is : '|' (Alt Gr + key 1 on the keyboard)")
    lab3.pack()
    lab4 = Label(top, text="The negatif symbol is : '-' (the dash)")
    lab4.pack()
    lab4 = Label(top, text="You can use the logic form too. Example : (b ∧ ¬ a) ∨ (c ∧ ¬a) ")
    lab4.pack()
    lab4 = Label(top, text="The expressions need to be checked before compared ")
    lab4.pack()


def compare_variable_widow():
    """
    function use to build the second windows for comparing variables
    """
    win = Toplevel(gui)
    win.configure(background="light blue")
    win.title("Variable Settings")
    win.geometry("320x230")
    log_entry_var = Label(win, bg="white", fg="black", textvariable=varResult, justify='center')
    varResult.set("")
    #bad_variable = set(count_variable1).symmetric_difference(set(count_variable2))

    if len(count_variable1) <= len(count_variable2):
        var_String.set(str(count_variable2).strip('[]"').replace("'", "").replace(" ", ""))
        name_label_box = Label(win, text="Variable Proposition 2 before :", pady=10, bg="light grey", relief='raised').pack(
            fill=BOTH)
        var_entry1 = Label(win, bg="white", fg="black",anchor=W, text=var_String.get()).pack(fill=BOTH)
        name_label_box2 = Label(win, text="Variable Proposition 2 after :", pady=10, bg="light grey", relief='raised').pack(
            fill=BOTH)
        var_entry2 = Entry(win, bg="white", fg="black", textvariable=var_Given).pack(fill=BOTH)
        var_tuto1 = Label(win, text="Please translate the " + str(len(count_variable2)) + " variables gived to allow the", bg="light grey").pack(
            fill=BOTH)
        var_tuto2 = Label(win, text="program to compare the two proposals with same variables",
                          bg="light grey").pack(fill=BOTH)
        var_tuto3 = Label(win, text='Variable of proposition 1 : ' + str(count_variable1).strip('[]"').replace("'", "").replace(" ", ""),
                          bg="light grey").pack(fill=BOTH)
        bouton_go = Button(win, text=' Go ', fg='white', bg='green', bd=1, command=lambda: changing_variable(count_variable1)).pack(
            fill=BOTH)
        log_entry_var.pack(fill=BOTH)
    else:

        var_String.set(str(count_variable1).strip('[]"').replace("'", "").replace(" ", ""))
        name_label_box = Label(win, text="Variable Proposition 1 before", pady=10, bg="light grey", relief='raised')\
            .pack(fill=BOTH)
        var_entry1 = Label(win, bg="white",anchor=W, fg="black", text=var_String.get()).pack(fill=BOTH)
        name_label_box2 = Label(win, text="Variable Proposition 1 after", pady=10, bg="light grey", relief='raised')\
            .pack(fill=BOTH)
        var_entry2 = Entry(win, bg="white", fg="black", textvariable=var_Given).pack(fill=BOTH)
        var_tuto1 = Label(win, text="Please translate the " + str(len(count_variable1)) + " variables gived to allow the",
                          bg="light grey").pack(fill=BOTH)
        var_tuto2 = Label(win, text="program to compare the two proposals with same variables",
                          bg="light grey").pack(fill=BOTH)
        var_tuto3 = Label(win, text='Variable of proposition 2: ' + str(count_variable2).strip('[]"')
                          .replace("'", "").replace(" ", ""), bg="light grey").pack(fill=BOTH)

        bouton_go = Button(win, text=' Go ', fg='white', bg='green', bd=1, command=lambda: changing_variable(count_variable2)).pack(
            fill=BOTH)
        log_entry_var.pack(fill=BOTH)

    def changing_variable(list_field):
        """
        function use to change variable's name in the proposition
        """

        list_var_given = []
        for char_var in var_Given.get():
            if char_var in list_field:
                list_var_given.append(char_var)
                print("one variable")

            elif char_var in alphabet and char_var not in list_field:
                varResult.set(char_var + " not in proposition field ")
                log_entry_var.config(bg="orange red")

        if len(list_var_given) != len(list_field):
            varResult.set("To much variable given : " + str(len(list_var_given)))
            log_entry_var.config(bg="orange red")


def key(event):
    char_key = event.char
    id_widget = str(event.widget.winfo_name())

    if id_widget == '!text':
        if char_key == '-':
            print(logic_entry1.index(INSERT))

            logic_entry1.insert(logic_entry1.index(INSERT), '¬')
            logic_entry1.delete("insert-2c")

        elif char_key == 'v' or char_key == 'V' or char_key == '*':
            logic_entry1.insert(logic_entry1.index(INSERT), '∨')
            logic_entry1.delete("insert-2c")

        elif char_key == '&' or char_key == 'é' or char_key == '+':
            logic_entry1.insert(logic_entry1.index(INSERT), '∧')
            logic_entry1.delete("insert-2c")

    elif id_widget == '!text2':
        if char_key == '-':
            logic_entry2.insert(logic_entry2.index(INSERT), '¬')
            logic_entry2.delete("insert-2c")

        elif char_key == 'v' or char_key == 'V' or char_key == '*':
            logic_entry2.insert(logic_entry2.index(INSERT), '∨')
            logic_entry2.delete("insert-2c")

        elif char_key == '&' or char_key == 'é' or char_key == '+':
            logic_entry2.insert(logic_entry2.index(INSERT), '∧')
            logic_entry2.delete("insert-2c")


def bracket_inspector(event):
    id_widget = str(event.widget.winfo_name())

    for tag1 in logic_entry1.tag_names():
        logic_entry1.tag_delete(tag1)
    for tag2 in logic_entry2.tag_names():
        logic_entry2.tag_delete(tag2)

    if id_widget == '!text':
        row0, col0 = logic_entry1.index(INSERT).split('.')
        row1, col1 = logic_entry1.index('1.end').split('.')

        if logic_entry1.get(logic_entry1.index(INSERT)) == '(':
            pos_bracket = 0.0
            count_bracket = 0

            for col_int in range(int(col0)+1, int(col1)):

                current_index = '1.' + str(col_int)
                if logic_entry1.get(current_index) == ')' and count_bracket == 0:
                    pos_bracket = current_index
                    logic_entry1.tag_add("ok start", logic_entry1.index(INSERT))
                    logic_entry1.tag_add("ok end", pos_bracket)
                    logic_entry1.tag_config("ok start", background="light green", foreground="blue")
                    logic_entry1.tag_config("ok end", background="light green", foreground="blue")
                    break
                elif logic_entry1.get(current_index) == '(':
                    count_bracket += 1
                    continue
                elif logic_entry1.get(current_index) == ')' and count_bracket != 0:
                    count_bracket -= 1
                else:
                    continue
            if pos_bracket == 0.0:
                logic_entry1.tag_add("KO", logic_entry1.index(INSERT))
                logic_entry1.tag_config("KO", background="orange red", foreground="white")

        elif logic_entry1.get(logic_entry1.index('insert-1c')) == ')':
            pos_bracket = 10.0
            count_bracket = 0

            for col_int in range(int(col0)-2, -1, -1):

                current_index = '1.' + str(col_int)
                if logic_entry1.get(current_index) == '(' and count_bracket == 0:
                    pos_bracket = current_index
                    # print(pos_bracket)
                    logic_entry1.tag_add("ok start", logic_entry1.index('insert-1c'))
                    logic_entry1.tag_add("ok end", pos_bracket)
                    logic_entry1.tag_config("ok start", background="light green", foreground="blue")
                    logic_entry1.tag_config("ok end", background="light green", foreground="blue")
                    break
                elif logic_entry1.get(current_index) == ')':
                    count_bracket += 1
                    continue
                elif logic_entry1.get(current_index) == '(' and count_bracket != 0:
                    count_bracket -= 1
                else:
                    continue
            if pos_bracket == 10.0:
                logic_entry1.tag_add("KO", logic_entry1.index('insert-1c'))
                logic_entry1.tag_config("KO", background="orange red", foreground="white")

    elif id_widget == '!text2':
        row0, col0 = logic_entry2.index(INSERT).split('.')
        row1, col1 = logic_entry2.index('1.end').split('.')

        if logic_entry2.get(logic_entry2.index(INSERT)) == '(':
            pos_bracket = 0.0
            count_bracket = 0

            for col_int in range(int(col0) + 1, int(col1)):

                current_index = '1.' + str(col_int)
                if logic_entry2.get(current_index) == ')' and count_bracket == 0:
                    pos_bracket = current_index
                    # print(pos_bracket)
                    logic_entry2.tag_add("ok start", logic_entry2.index(INSERT))
                    logic_entry2.tag_add("ok end", pos_bracket)
                    logic_entry2.tag_config("ok start", background="light green", foreground="blue")
                    logic_entry2.tag_config("ok end", background="light green", foreground="blue")
                    break
                elif logic_entry2.get(current_index) == '(':
                    count_bracket += 1
                    continue
                elif logic_entry2.get(current_index) == ')' and count_bracket != 0:
                    count_bracket -= 1
                else:
                    continue
            if pos_bracket == 0.0:
                logic_entry2.tag_add("KO", logic_entry2.index(INSERT))
                logic_entry2.tag_config("KO", background="orange red", foreground="white")

        elif logic_entry2.get(logic_entry2.index('insert-1c')) == ')':
            pos_bracket = 10.0
            count_bracket = 0

            for col_int in range(int(col0)-2, -1, -1):
                current_index = '1.' + str(col_int)
                if logic_entry2.get(current_index) == '(' and count_bracket == 0:
                    pos_bracket = current_index
                    # print(pos_bracket)
                    logic_entry2.tag_add("ok start", logic_entry2.index('insert-1c'))
                    logic_entry2.tag_add("ok end", pos_bracket)
                    logic_entry2.tag_config("ok start", background="light green", foreground="blue")
                    logic_entry2.tag_config("ok end", background="light green", foreground="blue")
                    break
                elif logic_entry2.get(current_index) == ')':
                    count_bracket += 1
                    continue
                elif logic_entry2.get(current_index) == '(' and count_bracket != 0:
                    count_bracket -= 1
                else:
                    continue
            if pos_bracket == 10.0:
                logic_entry2.tag_add("KO", logic_entry2.index('insert-1c'))
                logic_entry2.tag_config("KO", background="orange red", foreground="white")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Logic Comparator Pro")
    for e in range(4,5):
        gui.rowconfigure(e, weight=1)
        #gui.columnconfigure(e, weight=1)
    gui.geometry("800x500")
    #gui.resizable(False, False)
    logic1 = StringVar()
    logic2 = StringVar()
    log1 = StringVar()
    log2 = StringVar()
    var_String = StringVar()
    var_Given = StringVar()
    logicResult = StringVar()
    varResult = StringVar()

    logic1.set('(¬(a∨b)∨(c∧d))∧(¬a∨b)')
    logic2.set('(¬a∨c)∧(¬a∨d)∧(¬b∨c)∧(¬b∨d)∧(¬a∨b)')

    #for az in range(5):
        #for ae in range(5):
            #Button(gui, text='0', borderwidth=1).grid(row=az, column=ae)

    name_label1 = Label(gui, text="Logic Proposition 1", pady=2, bg="light grey", relief='raised').grid(row=0, column=0, sticky=W+N+E+S)
    name_label2 = Label(gui, text="Logic Proposition 2", pady=2, bg="light grey", relief='raised').grid(row=1, column=0, sticky=W+N+E+S)
    name_label3 = Label(gui, text="Validate :", pady=2, bg="light grey", relief='raised').grid(row=0, column=2,
                                                                                                        sticky=W + N + E + S)
    name_label4 = Label(gui, text="Validate :", pady=2, bg="light grey", relief='raised').grid(row=1, column=2,
                                                                                                        sticky=W + N + E + S)

    logic_entry1 = Text(gui, bg="white", fg="black", height=2, width=40)
    logic_entry1.grid(row=0, column=1, sticky=W+N+E+S)
    logic_entry1.insert(INSERT, str(logic1.get()))
    logic_entry1.bind("<KeyRelease>", key)
    logic_entry1.bind("<ButtonRelease-1>", bracket_inspector)
    logic_entry1.bind('<KeyRelease-Left>', bracket_inspector)
    logic_entry1.bind('<KeyRelease-Right>', bracket_inspector)
    logic_entry2 = Text(gui, bg="white", fg="black", height=2, width=40)
    logic_entry2.grid(row=1, column=1, sticky=W+N+E+S)
    logic_entry2.insert(INSERT, str(logic2.get()))
    logic_entry2.bind("<KeyRelease>", key)
    logic_entry2.bind("<ButtonRelease-1>", bracket_inspector)
    logic_entry2.bind('<KeyRelease-Left>', bracket_inspector)
    logic_entry2.bind('<KeyRelease-Right>', bracket_inspector)

    log_entry1 = Label(gui, bg="white", fg="black", textvariable=log1, justify='center', width=40)
    log_entry1.grid(row=0, column=3, sticky=W+N+E+S)
    log_entry2 = Label(gui, bg="white", fg="black", textvariable=log2, justify='center', width=40)
    log_entry2.grid(row=1, column=3, sticky=W+N+E+S)

    bouton_before1 = Button(gui, text=' ↩ ', fg='white', bg='cornflower blue', pady=0.5, bd=2, command=lambda: before(1)).grid(row=0, column=4, sticky=W+N+E+S)
    bouton_before2 = Button(gui, text=' ↩ ', fg='white', bg='cornflower blue', bd=2, pady=0.5, command=lambda: before(2)).grid(row=1, column=4, sticky=W+N+E+S)

    bouton_compare = Button(gui, text=' Compare ', fg='white', bg='green', bd=2, command=lambda: compare()).grid(row=2, column=0, sticky=W+N+E+S)
    logic_entry3 = Label(gui, bg="white", fg="black", textvariable=logicResult, justify='center')
    logic_entry3.grid(row=2, column=1, columnspan=3, sticky=W+N+S+E)

    bouton_reset = Button(gui, text=' Reset ', fg='white', bg='red', padx=10, bd=2, command=lambda: reset()).grid(row=2, column=3, sticky=N+E)
    bouton_question = Button(gui, text=' ? ', fg='black', bg='yellow', bd=2, command=lambda: compare_variable_widow()).grid(row=2, column=4, sticky=W+N+E+S)

    text = ('One', 'Two', 'Three', 'Four', 'Five')
    spin_historic = Spinbox(gui,values=text, width=10)

    scrollbar = Scrollbar(gui)
    mylist = Listbox(gui, yscrollcommand=scrollbar.set)
    gui.mainloop()
