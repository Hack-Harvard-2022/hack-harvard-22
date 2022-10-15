import PySimpleGUI as sg

def print_result(input, fixed):
    layout = [[sg.Text("Your speech: ")],
    [sg.Text(input)],
    [sg.Text("Modified: ")],
    [sg.Text(fixed)]
    ]

    window = sg.Window("SpeechLearn", layout, margins = (300,200))

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
    window.close()
    return

def main():
    layout = [[sg.Text("Welcome to SpeechLearn")], [sg.Text("Click to record")], [sg.Button("RECORD")]]
    # create window
    window = sg.Window("SpeechLearn", layout, margins = (300,200))

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

        if event == "RECORD":
            input_str = "I no eat hot dog."
            fixed_str = "I do not eat hot dogs."
            print_result(input_str, fixed_str)

    window.close()

if __name__ == "__main__":
    main()

