from sys import breakpointhook
import PySimpleGUI as sg
import argparse
import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
from record_arbitrary import *

def recording():
    layout = [[sg.Text("Recording...")], [sg.Text("Click to stop")], [sg.Button("STOP")]]

    window = sg.Window("SpeechLearn", layout, margins = (300,200))

    parser = create_parser()
    args = parser.parse_args()
    q = setup_record(parser, args)

    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                      channels=args.channels, subtype=args.subtype) as file:
        with sd.InputStream(samplerate=args.samplerate, device=args.device,
                            channels=args.channels, callback=callback):
            while True:
                file.write(q.get())
                event, values = window.read()
                if event in (None, 'Exit'):
                    parser.exit(0)
                    break

                if event == "STOP":
                    parser.exit(0)
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