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
check_count = 0
nb_variable = 0
count_variable1 = []
count_variable2 = []
truth_table_list = []


def check():
    """
    This is the check function called by the check button
    The goal of this function is to check if the 2 inputs (the 2 logical expressions)
    are valid syntaxicaly and lexicaly
    """
    global nb_variable, check_count, normal_form_1, normal_form_2, list1, list2, count_variable2, count_variable1

    logicResult.set("")
    print(check_count)

    if check_count == 0:
        count_variable1 = []
        count_variable2 = []
        count_bad_1 = []
        count_bad_2 = []
        normal_form_1 = str(logic1.get())
        normal_form_2 = str(logic2.get())
        list1 = list(normal_form_1)
        list2 = list(normal_form_2)
        #print(list1)
        #print(list2)

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

        if len(count_bad_1) > 0 or len(count_bad_2) > 0:
            logic1.set("Bad entry, unresolved symbol : " + str(count_bad_1))
            logic2.set("Bad entry, unresolved symbol : " + str(count_bad_2))

        elif len(count_variable1) != len(count_variable2):
            logic1.set("Bad entry, different number of variable : " + str(count_variable1) +
                       " variables")
            logic2.set("Bad entry, different number of variable : " + str(count_variable2) +
                       " variables")

        elif len(set(count_variable1).intersection(set(count_variable2))) != len(count_variable1):
            logic1.set("Bad entry, not the same variable : " + str(count_variable1))
            logic2.set("Bad entry, not the same variable : " + str(count_variable2))

        else:
            logic1.set("Entry ok")
            logic2.set("Entry ok")
            nb_variable = len(count_variable1)
        check_count += 1
    else:
        if (normal_form_1 == str(logic1.get()) and normal_form_2 == str(logic2.get())) or logic1.get() == "Entry ok"  \
                or logic1.get().find("Bad entry") != -1:
            logic1.set("the inspection has already been done.")
            logic2.set("the inspection has already been done.")
        else:
            check_count = 0
            check()


def true_table_canvas(table):
    """
    This is the true_table_canvas called in the compare function
    if the comparaison was made and a result is gived
    :param table:
    """

    mylist.insert(END, 'Here is the table of truth found :')
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
    mylist.pack(fill=BOTH)
    scrollbar.config(command=mylist.yview)


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
    global nb_variable, check_count, normal_form_1, normal_form_2, list1, list2, count_variable2, count_variable1,\
        truth_table_list
    logic1.set('enter your first logic expression')
    logic2.set('enter your second logic expression')
    logicResult.set("")
    normal_form_1 = ""
    normal_form_2 = ""
    list1 = []
    list2 = []
    count_variable1 = []
    count_variable2 = []
    truth_table_list = []
    check_count = 0
    nb_variable = 0

    #print(truth_table_list)


def compare():
    """
    This is the compare function called in the compare button.
    The goal of this fucntion is to compare the 2 inputs and give the result to
    the user(s). The 2 inputs need to be checked before compared
    """
    global truth_table_list, check_count
    if check_count > 0:

        truth_table_list = []
        logic1.set(normal_form_1)
        logic2.set(normal_form_2)
        logic_table_instance = list(itertools.product('01', repeat=nb_variable))

        #print(logic_table_instance)

        normal_form_1_format = format_logic(normal_form_1)
        normal_form_2_format = format_logic(normal_form_2)

        #print(normal_form_1, id(normal_form_1))
        #print(normal_form_1_format, id(normal_form_1_format))
        #print(normal_form_2, id(normal_form_2))
        #print(normal_form_2_format, id(normal_form_2_format))

        for e in range(0, len(logic_table_instance)):
            normal_form_1_format_copy = normal_form_1_format
            normal_form_2_format_copy = normal_form_2_format
            for i in range(0, len(count_variable1)):
                normal_form_1_format_copy = normal_form_1_format_copy.replace(count_variable1[i],
                                                                              logic_table_instance[e][i])
                normal_form_2_format_copy = normal_form_2_format_copy.replace(count_variable1[i],
                                                                              logic_table_instance[e][i])

            normal_form_1_format_copy_final = normal_form_1_format_copy.replace("-0", "1").replace("-1", "0")\
                .replace("- 0", "1").replace("- 1", "0")
            normal_form_2_format_copy_final = normal_form_2_format_copy.replace("-0", "1").replace("-1", "0")\
                .replace("- 0", "1").replace("- 1", "0")

            try:
                eval(normal_form_1_format_copy_final)
                eval(normal_form_2_format_copy_final)
            except SyntaxError:
                logic1.set("Syntax Error")
                logic2.set("Syntax Error")

            truth_table_list.append((logic_table_instance[e], eval(normal_form_1_format_copy_final),
                                     eval(normal_form_2_format_copy_final)))

            #print(normal_form_1_format_copy_final, normal_form_2_format_copy_final)
        #print(truth_table_list)

        logicResult.set("They're equal")
        for test in range(0, len(truth_table_list)):
            if truth_table_list[test][1] != truth_table_list[test][2]:
                logicResult.set("Not Equal")
                break
            else:
                continue

        true_table_canvas(truth_table_list)
        check_count = 0

    else:
        logicResult.set("Check not done")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Logic Comparator Pro")
    gui.geometry("800x500")

    logic1 = StringVar()
    logic2 = StringVar()
    logicResult = StringVar()

    name_label1 = Label(gui, text="Logic Proposition 1", pady=10, bg="light grey", relief='raised').pack(fill=X)
    logic_entry1 = Entry(gui, bg="white", fg="black", textvariable=logic1).pack(fill=BOTH)
    name_label2 = Label(gui, text="Logic Proposition 2", pady=10, bg="light grey", relief='raised').pack(fill=BOTH)
    logic_entry2 = Entry(gui, bg="white", fg="black", textvariable=logic2).pack(fill=BOTH)
    bouton_check = Button(gui, text=' Check ', fg='white', bg='blue', bd=4, command=lambda: check()) \
        .pack(fill=BOTH, padx=350, pady=5)
    bouton_compare = Button(gui, text=' Compare ', fg='white', bg='green', bd=4, command=lambda: compare()) \
        .pack(fill=BOTH, padx=350, pady=5)

    logic_entry3 = Entry(gui, bg="white", fg="black", textvariable=logicResult).pack(fill=BOTH, padx=350)

    bouton_reset = Button(gui, text=' Reset ', fg='white', bg='red', bd=4, command=lambda: reset()) \
        .pack(fill=BOTH, padx=350, pady=5)

    scrollbar = Scrollbar(gui)
    scrollbar.pack(fill=BOTH)
    mylist = Listbox(gui, yscrollcommand=scrollbar.set)

    logic1.set('Enter your first logic expression')
    logic2.set('Enter your second logic expression')
    #logic1.set('(b & - a) | (c & -a)')
    #logic2.set('(b | c) & -a')
    #logic1.set('(b ∧ ¬ a) ∨ (c ∧ ¬a)')
    #logic2.set('(b ∨ c) ∧ ¬a')
    #'∨', '∧' ¬
    gui.mainloop()
