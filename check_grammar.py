import language_tool_python
import requests

def internet_on():
    try:
        requests.get(url = "https://google.com")
        return True
    except: 
        return False

def initialize_tool(language='en_US'):
    if not internet_on():
        tool = language_tool_python.LanguageTool(language)
    else:
        tool = language_tool_python.LanguageToolPublicAPI(language)
    return tool

def analyze_string(tool, input_str):
    return tool.check(input_str)

def correct_string(matches, input_str):
    is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    return language_tool_python.utils.correct(input_str, matches)






