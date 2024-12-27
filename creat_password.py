# Amir Farzadi
# instagram id: @realamirr_7
# gmail: amirfarzadi80@gmail.com


import string
from tkinter import *
import random

if __name__ == "__main__":
    is_upper_case_allowed = False
    is_digits_allowed = False
    is_punctuation_allowed = False
    # =========================Main Window=================================
    main_window = Tk()
    main_window.geometry("360x400")
    main_window.title("Create Password")
    main_window.resizable(False, False)

    # ===========================Variables===================================
    entry_length_result = StringVar()
    entry_length_result.set("0")

    # =========================Frame=================================
    Frame(master=main_window, background="cyan", width=360, height=400).pack(anchor="center")

    # =========================Entry=================================
    length_entry = Entry(main_window, textvariable=entry_length_result, width=8, font='airal 15', background="white",
                         foreground="red")
    length_entry.place(x=250, y=10)

    # =========================Label=================================
    length_label = Label(main_window, text="insert password length:", foreground="red", width=20, font="arial 15")
    length_label.place(x=5, y=10)

    upper_case_label = Label(main_window, text="upper", foreground="red", width=10, font="arial 15")
    upper_case_label.place(x=5, y=50)

    digits_label = Label(main_window, text="digits", foreground="red", width=10, font="arial 15")
    digits_label.place(x=5, y=90)

    punctuation_label = Label(main_window, text="punctuation", foreground="red", width=10, font="arial 15")
    punctuation_label.place(x=5, y=130)

    # =========================Functions=================================

    def set_variable_true(item: str):
        global is_upper_case_allowed
        global is_digits_allowed
        global is_punctuation_allowed

        if item == "upper":
            is_upper_case_allowed = True if is_upper_case_allowed is False else False

        elif item == "digits":
            is_digits_allowed = True if is_digits_allowed is False else False

        elif item == "punctuation":
            is_punctuation_allowed = True if is_punctuation_allowed is False else False


    def create_password(length: int = 8,  use_upper_case=is_upper_case_allowed, use_digits=is_digits_allowed,
                        punctuation=is_punctuation_allowed):

        password = ""
        if use_digits:
            password += string.digits

        if use_upper_case:
            password += string.ascii_uppercase

        if punctuation:
            password += string.punctuation

        if len(password) < 4:
            password += string.ascii_letters

        if length < 4:
            length = 4
        return "".join(random.choices(password, k=length))

    def button_set_function():
        global is_upper_case_allowed
        global is_digits_allowed
        global is_punctuation_allowed
        password = create_password(int(entry_length_result.get()), is_upper_case_allowed, is_digits_allowed,
                                   is_punctuation_allowed)
        label = Label(main_window, background="green", foreground="black", width=30, font="arial 15",
                      text=f"password : {password}")

        label.place(x=40, y=300)

        # main_window.after(6000, main_window.destroy)

    # =========================Check Boxs=================================

    upper_case_check_box = Checkbutton(main_window, background="red", foreground="red",
                                       command=lambda: set_variable_true("upper"))
    upper_case_check_box.place(x=150, y=50)

    digits_check_box = Checkbutton(main_window, background="red", foreground="red",
                                   command=lambda: set_variable_true("digits"))
    digits_check_box.place(x=150, y=90)

    punctuation_check_box = Checkbutton(main_window, background="red", foreground="red",
                                        command=lambda: set_variable_true("punctuation"))
    punctuation_check_box.place(x=150, y=130)

    # =========================Buttons=================================
    set_button = Button(main_window, text="set",   background="black", foreground="Red", width=15, font="arial 15 bold",
                        command=lambda: button_set_function())
    set_button.place(x=80, y=200)

    main_window.mainloop()
