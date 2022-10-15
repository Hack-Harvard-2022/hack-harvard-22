from sys import breakpointhook
import PySimpleGUI as sg

def recording():
    layout = [[sg.Text("Recording...")], [sg.Text("Click to stop")], [sg.Button("STOP")]]

    window = sg.Window("SpeechLearn", layout, margins = (300,200))

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

        if event == "STOP":
            break
    window.close()
    return

def main():
    layout = [[sg.Text("Welcome to SpeechLearn")], [sg.Text("Click to record")], [sg.Button("RECORD")]]

    # create window
    window = sg.Window("SpeechLearn", layout, margins = (300,200))

    # create an event loop
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        # ends program if window closed or user clicks OK
        if event == "RECORD":
            recording()
            # stop button appears
            # record_speech.py
            # speech_to_text.py
            # outputs speech text in a box
            # outputs corrected speech text in a box
    window.close()

if __name__ == "__main__":
    main()