# Program #1: MPG Calculator
# Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let
# the user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked, the program should
# display the number of miles that the car may be driven per gallon of gas.
# Use the following formula to calculate miles per gallon:  MPG = miles / gallons.

import tkinter as tk
import tkinter.messagebox

class MyGUI():

    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("MPG Calculator")

        # Create frames
        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create top frame widgets
        self.capacity_label = tk.Label(self.top_frame, text='Enter the fuel capacity of your car in gallons:')
        self.capacity_entry = tk.Entry(self.top_frame, width=10)

        # Pack top frame widgets
        self.capacity_label.pack(side='left')
        self.capacity_entry.pack(side='left')

        # Create middle frame widgets
        self.miles_label = tk.Label(self.middle_frame, text='Enter the number of miles that can be driven on a full tank:')
        self.miles_entry = tk.Entry(self.middle_frame, width=10)

        # Pack middle frame widgets
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create buttons for bottom frame
        self.calc_button = tk.Button(self.bottom_frame, text='Calculate MPG', command=self.calc)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

        # Calculate method
    def calc(self):
        try:
            capacity = float(self.capacity_entry.get())

            miles = float(self.miles_entry.get())

            MPG = miles / capacity

            tkinter.messagebox.showinfo('Results', f'Your car can go {MPG:.2f} miles per gallon.')
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Please enter valid numbers')

if __name__ == '__main__':
    MyGUI()
