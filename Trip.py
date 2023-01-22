import PySimpleGUI as sg

# Function to calculate trip time
def trip_time(tms, i_double_prime, fault_current, curve_type):
    tms = float(tms)
    i_double_prime = float(i_double_prime)
    fault_current = float(fault_current)
    Is = i_double_prime
    I = fault_current
    if curve_type == "IEC standard inverse curve":
        k, alpha = 0.140, 0.020
    elif curve_type == "IEC very inverse curve":
        k, alpha = 13.5, 1
    elif curve_type == "IEC extremely inverse curve":
        k, alpha = 80, 2
    elif curve_type == "IEC long time standard inverse curve":
        k, alpha = 120, 1
    else:
        return None

    trip_time = tms * (k / ((I/Is) ** alpha - 1))
    trip_time = round(trip_time, 3)
    return trip_time

# Layout for the GUI
layout = [
    [sg.Text("TMS"), sg.Input(key="tms")],
    [sg.Text("I>"), sg.Input(key="i_double_prime")],
    [sg.Text("Fault current"), sg.Input(key="fault_current")],
    [sg.Text("Curve type"), sg.Combo(["IEC standard inverse curve", "IEC very inverse curve", "IEC extremely inverse curve", "IEC long time standard inverse curve"], key="curve_type")],
    [sg.Button("Calculate"), sg.Button("Cancel")],
    [sg.Text("Trip time: "), sg.Text("", key="trip_time")],
    [sg.Text("                                                         Author: tkahawalage PSD Energy ")]
]

# Create the GUI window
window = sg.Window("Trip Time Calculator", layout)

# Event loop to handle user inputs
while True:
    event, values = window.read()
    if event == "Calculate":
        tms = values["tms"]
        i_double_prime = values["i_double_prime"]
        fault_current = values["fault_current"]
        curve_type = values["curve_type"]
        trip_time_value = trip_time(tms, i_double_prime, fault_current, curve_type)
        if trip_time_value is not None:
            window["trip_time"].update(str(trip_time_value) + 's')
    elif event == "Cancel" or event == sg.WIN_CLOSED:
        break

window.close()