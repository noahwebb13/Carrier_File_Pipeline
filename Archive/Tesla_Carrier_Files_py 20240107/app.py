import tkinter as tk
import os
import json
from module import read
from module import map 
from module import concat_and_map
from module import pivot_carrier_files

# setting app working directoy
os.chdir("C:/Users/nwebb19/python/Tesla_Carrier_Files_py")

carrier1 = 'Aetna'
carrier2 = 'VSP'

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
# button5 = tk.Button(window, text="Create Carrier Pivot", command = pivot_carrier_files)

# pack the button widget into the window
button1.pack()
button2.pack()

# Start the Tkinter event loop
window.mainloop()