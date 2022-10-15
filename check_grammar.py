import language_tool_python
import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def initialize_tool(language='en_US'):
    if not internet_on():
        tool = language_tool_python.LanguageTool(language)
    else:
        tool = language_tool_python.LanguageToolPublicAPI(language)
    return tool

def analyze_string(tool, input_str):
    matches = tool.check(input_str)

#input_str = input("enter your sentence: ")
input_str = "you no do laundry"



