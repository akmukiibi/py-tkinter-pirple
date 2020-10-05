"""
    Assignment on Importing
    Chosen Library is Tkinter for GUI
    Author: Alvin Mukiibi
"""

import tkinter as tk  # bring in the tkinter GUI library
import db as database  # bring in our db class
import tkinter.messagebox as messagebox

db = database.Database('users.db')


# our functions

def populate_list():
    people_list.delete(0, tk.END)  # first delete whoever is on the list
    for row in db.fetch():  # fetch people from our db and insert them into the list
        people_list.insert(tk.END, row)


def add_item():
    # some validation i.e. if user misses any field
    if name_value.get() == '' or age_value.get() == '' or ms_value.get() == '' or contact_value.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    # insert into the db
    db.insert(name_value.get(), age_value.get(), ms_value.get(), contact_value.get())
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = people_list.curselection()[0]  # get the selected person on the list
        selected_item = people_list.get(index)

        name_value.delete(0, tk.END)  # remove whatever is in that field and put the selected one
        name_value.insert(tk.END, selected_item[1])
        age_value.delete(0, tk.END)
        age_value.insert(tk.END, selected_item[2])
        ms_value.delete(0, tk.END)
        ms_value.insert(tk.END, selected_item[3])
        contact_value.delete(0, tk.END)
        contact_value.insert(tk.END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    """
    Deleted selected item from db, just invoke our db api and send in the id
    :return:
    """
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], name_value.get(), age_value.get(), ms_value.get(), contact_value.get())
    populate_list()


def clear_text():
    name_value.delete(0, tk.END)
    age_value.delete(0, tk.END)
    ms_value.delete(0, tk.END)
    contact_value.delete(0, tk.END)


window = tk.Tk()  # initiate a window object using tkinter's TK method

window.title('Town Directory')  # change title of the window
window.geometry('700x300')  # change the dimensions of the window

""" Now we are to start adding widgets"""

name = tk.StringVar()
name_label = tk.Label(window, text="Name", font=('bold', 12), pady=20)
name_label.grid(row=0, column=0, sticky=tk.W)  # sticky is to align the label to the West(W) which is the left
name_value = tk.Entry(window, textvariable=name)
name_value.grid(row=0, column=1)

age = tk.IntVar()  # remember age is an int in the DDL
age_label = tk.Label(window, text="Age", font=('bold', 12))
age_label.grid(row=0, column=2, sticky=tk.W)  # sticky is to align the label to the West(W) which is the left
age_value = tk.Entry(window, textvariable=age)  # this is the input
age_value.grid(row=0, column=3)

marital_status = tk.StringVar()
ms_label = tk.Label(window, text="Marital Status", font=('bold', 12))
ms_label.grid(row=1, column=0, sticky=tk.W)
ms_value = tk.Entry(window, textvariable=marital_status)
ms_value.grid(row=1, column=1)

contact = tk.StringVar()
contact_label = tk.Label(window, text="Contact", font=('bold', 12))
contact_label.grid(row=1, column=2, sticky=tk.W)
contact_value = tk.Entry(window, textvariable=contact)
contact_value.grid(row=1, column=3)

# peoples list
people_list = tk.Listbox(window, height=8, width=50)
people_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# scroll bar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=3, column=3)

# set scrollbar to list box to be vertical i.e. yscrollcommand
people_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=people_list.yview)
# bind select
people_list.bind('<<ListboxSelect>>', select_item)

# add buttons

add_btn = tk.Button(window, text="Add Person", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = tk.Button(window, text="Remove Person", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = tk.Button(window, text="Update Person", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = tk.Button(window, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# populate db
populate_list()

window.mainloop()  # run the main window
