from gramformer import Gramformer
import torch
import language_tool_python
import requests

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

def internet_on():
    try:
        requests.get(url = "https://google.com")
        return True
    except: 
        return False

def initialize_tool(language='en_US'):
    tool = language_tool_python.LanguageTool(language)
    return tool
    '''
    if language == 'en_US':
        set_seed(1212)
        gf = Gramformer(models = 1, use_gpu=False)
    if not internet_on():
        tool = language_tool_python.LanguageTool(language)
    else:
        tool = language_tool_python.LanguageToolPublicAPI(language)
    return [tool, gf]'''

def analyze_string(tool, input_str):
    return correct_string(tool.check(input_str), input_str)
    try:
        return tool[1].correct(input_str, max_candidates=1)
    except:
        return correct_string(tool.check(input_str), input_str)
def correct_string(matches, input_str):
    is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    return language_tool_python.utils.correct(input_str, matches)




