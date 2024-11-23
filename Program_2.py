# Joe's Automotive performs the following routine
# maintenance service:

# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00

# Write a GUI with check buttons that allows
# the user to select any or all of these services.
# When the user clicks a button, the total charges
# should be displayed.

import tkinter as tk
import tkinter.messagebox

class MyGUI:

    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Joe's Automotive Services")

        # Create frames
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create check buttons
        self.oil_change = tkinter.IntVar()
        self.lube_job = tkinter.IntVar()
        self.radiator_flush = tkinter.IntVar()
        self.transmission_fluid = tkinter.IntVar()
        self.inspection = tkinter.IntVar()
        self.muffler_replacement = tkinter.IntVar()
        self.tire_rotation = tkinter.IntVar()

        # Set the IntVar objects to 0
        self.oil_change.set(0)
        self.lube_job.set(0)
        self.radiator_flush.set(0)
        self.transmission_fluid.set(0)
        self.inspection.set(0)
        self.muffler_replacement.set(0)
        self.tire_rotation.set(0)

        # create check buttons in top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30', variable = self.oil_change)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20', variable=self.lube_job)
        self.cb3 =tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40', variable=self.radiator_flush)
        self.cb4 =tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100', variable=self.transmission_fluid)
        self.cb5 =tkinter.Checkbutton(self.top_frame, text='Inspection - $35', variable=self.inspection)
        self.cb6 =tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200', variable=self.muffler_replacement)
        self.cb7 =tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20', variable=self.tire_rotation)

        # Pack the check buttons
        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')

        # Create buttons for bottom frame
        self.OK_button = tk.Button(self.bottom_frame, text='OK', command=self.show_price)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons
        self.OK_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

    def show_price(self):

        total_charge = 0

        if self.oil_change.get() == 1:
            total_charge += 30
        if self.lube_job.get() == 1:
            total_charge += 20
        if self.radiator_flush.get() == 1:
            total_charge += 40
        if self.transmission_fluid.get() == 1:
            total_charge += 100
        if self.inspection.get() == 1:
            total_charge += 35
        if self.muffler_replacement.get() == 1:
            total_charge += 200
        if self.tire_rotation.get() == 1:
            total_charge += 20

        tk.messagebox.showinfo("Total Charges", f"Total charges for selected services: ${total_charge:.2f}")

if __name__ == '__main__':
    MyGUI()
