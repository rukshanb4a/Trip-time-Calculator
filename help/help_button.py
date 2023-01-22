import PySimpleGUI as sg

layout = [
    [sg.Text("Parameter1"), sg.InputText()],
    [sg.Text("Parameters2"), sg.InputText()],
    [sg.Submit(), sg.Cancel(), sg.ReadFormButton('Help')]
]

form = sg.FlexForm('Test GUI')
form.Layout(layout)

# ---- Event Loop ---- # necessary to catch help click
while True:

    button, values = form.Read()

    # ---- Process Button Clicks ---- #
    if button == "Submit":
        Parameters1, Parameters2 = values
        break  # to quit the loop

    elif button == 'Help':
        sg.Popup("My help message")

    elif button == "Cancel":
        break