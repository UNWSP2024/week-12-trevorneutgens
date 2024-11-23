# Program #3 Long-Distance Calls
# A long-distance provider charges the following rates
# for telephone calls:

# Rate Category	Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05

# Write a GUI application that allows the user to select
# a rate category (from a set of radio buttons), and enter
# the number of minutes of the call into an Entry widget.
# An info dialog box should display the charge for the call.


import tkinter as tk


class MyGUI:

    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Calls")

        # Create frames
        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.result_frame = tk.Frame(self.main_window)

        # Create IntVar object
        self.radio_var = tk.IntVar()

        # Set the IntVar object to 0
        self.radio_var.set(0)

        # create radio buttons in top frame
        self.rb1 = tk.Radiobutton(self.top_frame, text='Daytime (6:00 A.M. through 5:59 P.M.) $0.02 per minute', variable = self.radio_var, value = 1)
        self.rb2 = tk.Radiobutton(self.top_frame, text='Evening (6:00 P.M.  through 11:59 P.M.) $0.12 per minute', variable=self.radio_var, value = 2)
        self.rb3 = tk.Radiobutton(self.top_frame, text='Off-Peak (midnight through 5:59 P.M.) $0.05 per minute',variable=self.radio_var, value = 3)

        # Pack the radio buttons
        self.rb1.pack(anchor='w')
        self.rb2.pack(anchor='w')
        self.rb3.pack(anchor='w')

        # Create time entry in middle frame
        self.time_label = tk.Label(self.middle_frame, text='Enter the number of minutes spoken on the phone:')
        self.time_entry = tk.Entry(self.middle_frame, width=10)

        # pack middle frame
        self.time_label.pack(side='left')
        self.time_entry.pack(side='left')

        # Create buttons for bottom frame
        self.OK_button = tk.Button(self.bottom_frame, text='OK', command=self.show_price)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons
        self.OK_button.pack(side='left')
        self.quit_button.pack(side='left')

        # label to display the result or errors
        self.result_label = tk.Label(self.result_frame, text='')

        # pack frames and result label
        self.top_frame.pack(pady=5)
        self.middle_frame.pack(pady=5)
        self.bottom_frame.pack(pady=5)
        self.result_frame.pack(pady=10)
        self.result_label.pack()


        tk.mainloop()

    def show_price(self):
        try:
            total_charge = 0
            minutes = float(self.time_entry.get())

            if self.radio_var.get() == 1:
                total_charge = minutes * 0.02
            elif self.radio_var.get() == 2:
                total_charge = minutes * 0.12
            elif self.radio_var.get() == 3:
                total_charge = minutes * 0.05
            else:
                self.result_label.config(text="Please select a time category.")
                return

            self.result_label.config(text=f"Total charges for the call: ${total_charge:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number of minutes.")


if __name__ == '__main__':
    MyGUI()
