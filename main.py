# main control flow
from check_grammar import *
from record_speech import *
from speech_to_text import *
import os


file = 'temp.wav'

time = int(input("enter time: "))

record_for_time(file, time)

input_str = speech_to_text(file)

print(check_grammar(input_str))

os.remove("temp.wav")
