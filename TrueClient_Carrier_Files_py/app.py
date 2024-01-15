import tkinter as tk
import os
import json
from module import *

# setting app working directoy
os.chdir("/Users/noahwebb/Python/Carrier_File_Pipeline/TrueClient_Carrier_Files_py")

carrier1 = 'RealMedCarrier'
carrier2 = 'RCRS'
carrier3 = 'Dentlife'
carrier4 = 'VisionSavings'

def run_concat_and_map(carrier):
    try: 
        #run the script using subprocess
        concat_and_map(carrier)

    except:
        # Handle any errors that occur during the script execution
        print("An error occured when running the script.")

# create main window
window = tk.Tk()

# set the window title
window.title("Carrier Files")

# Create a label 
label = tk.Label(
    window, 
    text=("Combine Carrier Files"),
    font=("Arial",20),
    fg="#FF612B",
    bg="#FAF8F2",
    padx=100,
    pady=10
)

# pack the label into the window
label.pack()

# Create a button widget
button1 = tk.Button(window, text=carrier1, command = lambda v=carrier1: run_concat_and_map(v))
button2 = tk.Button(window, text=carrier2, command = lambda v=carrier2: run_concat_and_map(v))
button3 = tk.Button(window, text=carrier3, command = lambda v=carrier3: run_concat_and_map(v))
button4 = tk.Button(window, text=carrier4, command = lambda v=carrier4: run_concat_and_map(v))
# button5 = tk.Button(window, text="Create Carrier Pivot", command = pivot_carrier_files)

# pack the button widget into the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# Start the Tkinter event loop
window.mainloop()