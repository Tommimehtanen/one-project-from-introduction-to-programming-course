# TIE-02100 Johdatus ohjelmointiin
# Graafinen käyttöliittymä ohjelma
# Joka laskee veren alkoholipitoisuuden promilleina nopeasti nautittuna.
# Ohjelmaan syötetään paino, sukupuoli ja annosten määrä.
# Näistä tiedoista ohjelma laskee alkoholin määrän veressä kyseisellä hetkellä
# Tommi Mehtänen 279330, Eetu Jokinen 273281

from tkinter import *


class User_interface:

    def __init__(self):
        self.__liquid_in_body = 0

        self.__alcohol_in_grams = 0
        self.__alcohol_in_blood = 0
        self.__factor = 0

        self.__err_msg = " "

        self.__mainwindow = Tk()
        self.__mainwindow.title("Blood alcohol calculator")

        self.__weight_label = Label(self.__mainwindow, text="Weight (kg)",
                                    background="beige")
        self.__gender_label = Label(self.__mainwindow,
                                    text="Gender (male/female)",
                                    background="beige")
        self.__units_label = Label(self.__mainwindow, text="Units consumed",
                                   background="beige")

        self.__alcohol_in_blood_label = Label(self.__mainwindow, text="0.00")
        self.__alcohol_in_blood_label.grid(row=1, column=3, columnspan=4,
                                           rowspan=2)
        self.__error_label = Label(self.__mainwindow, text=" ", fg="red")
        self.__error_label.grid(row=7, column=1, columnspan=2, sticky=N)

        self.__units_consumed = Entry()
        self.__weight_value = Entry()
        self.__gender_value = Entry()

        self.__weight_label.grid(row=1, column=1, sticky = E+W)
        self.__gender_label.grid(row=3, column=1, columnspan =2)
        self.__units_label.grid(row=5, column=1, sticky = E+W)

        self.__units_consumed.grid(row=6, column=1, sticky=E+W)
        self.__weight_value.grid(row=2, column=1, sticky=E+W)
        self.__gender_value.grid(row=4, column=1, sticky=E+W)

        self.__calculate_button = Button(self.__mainwindow, text="Calculate",
                                         bg="blue", fg="yellow", relief=GROOVE
                                         , padx=30, pady=10,
                                         activebackground="green",
                                         activeforeground="red",
                                         borderwidth=3,
                                         command=self.alcohol_in_blood)

        self.__calculate_button.grid(row=3, column=3, columnspan=4, rowspan=2)






    def gender_factor(self):
        """ Counts factor for male and female gender
        :return: none
        """
        if self.__gender_value.get() == "male":
            self.__factor = 0.75
        elif self.__gender_value.get() == "female":
            self.__factor = 0.66
        else:
            self.__factor = 0
            self.__err_msg = "Gender must be male or female"


    def liquid_in_body(self):
        """ Counts amount of liquid in users body
        :return: none
        """
        self.gender_factor()

        try:
            if int(self.__weight_value.get()) > 0:
                self.__liquid_in_body = self.__factor * int(
                    int(self.__weight_value.get()))
            else:
                self.__liquid_in_body = 0
                self.__err_msg = "Weight must be positive number!"
        except ValueError:
            self.__err_msg = "Weight must be positive number!"


    def alcohol_consumed(self):
        """ Counts alcohol consumed in grams
        :return: none
        """
        self.__alcohol_in_grams = int(self.__units_consumed.get()) * 12


    def alcohol_in_blood(self):
        """ Counts users alcohol amount in blood and shows it in label
        :return: none
        """
        self.liquid_in_body()
        self.alcohol_consumed()

        if self.__alcohol_in_grams < 0:
            self.__error_label.configure(text="Units consumed must be \
            positive number")
        elif self.__liquid_in_body > 0:

            # All values were valid

            self.__error_label.configure(text=" ")

            self.__alcohol_in_blood = int(self.__alcohol_in_grams)\
                                  / self.__liquid_in_body

            self.__alcohol_in_blood_label.configure(text= "{:0.2f}"\
                                .format(self.__alcohol_in_blood))
        else:
            self.__alcohol_in_blood_label.configure(text="0.00")
            self.__error_label.configure(text = self.__err_msg)


    def reset_fields(self):
        """ Resets label fields
        :return: none
        """
        self.__units_consumed.delete(0, END)
        self.__weight_value.delete(0, END)
        self.__gender_value.configure(text="")
        self.__error_label.delete(0, END)



    def start(self):
        """ Starts programs execution
        :return:
        """
        self.__mainwindow.mainloop()


def main():
    ui = User_interface()
    ui.start()
main()