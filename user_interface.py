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
import argparse
import tempfile
import queue
import sys
import _thread


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args()

def recording():
    layout = [[sg.Text("Recording...")], [sg.Text("Click to stop")], [sg.Button("STOP")]]

    window = sg.Window("SpeechLearn", layout, margins = (300,200))
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])
    if args.filename is None:
        args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                        suffix='.wav', dir='')
    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())
    
    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                      channels=args.channels, subtype=args.subtype) as file:
        with sd.InputStream(samplerate=args.samplerate, device=args.device,
                            channels=args.channels, callback=callback):
            def loop_function():
                while True:
                    file.write(q.get())
            while True:
                _thread.start_new_thread(loop_function, ())
                event, value = window.read()
                if event in (None, 'Exit'):
                    break
                if event == "STOP":
                    break
    window.close()
    parser.exit(0)
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