import language_tool_python
import requests

def __init__(self, language, string, tool = None):
    if not tool == None:
        self.initialize_tool(language)
    


def internet_on():
    try:
        requests.get(url = "https://google.com")
        return True
    except: 
        return False

def initialize_tool(self, language='en_US'):
    if not self.internet_on():
        tool = language_tool_python.LanguageTool(language)
    else:
        tool = language_tool_python.LanguageToolPublicAPI(language)
    return tool

def analyze_string(tool, input_str):
    matches = tool.check(input_str)





