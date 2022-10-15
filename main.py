# main control flow
from check_grammar import *
#from record_speech import *
#from speech_to_text import *



#test grammar
input_str = input("here: ")

tool = initialize_tool("en-US")
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)
input_str = str
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)
input_str = str
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)
input_str = str
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)
input_str = str
result = analyze_string(tool, input_str)
str = correct_string(result, input_str)
print(str)