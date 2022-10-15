# main control flow
from check_grammar import *
from record_speech import *
from speech_to_text import *


file = 'temp.wav'

time = int(input("enter time: "))

record_for_time(file, time)

input_str = speech_to_text(file)

tool = initialize_tool("en-US")
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)
