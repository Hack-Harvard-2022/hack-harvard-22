import torch
import language_tool_python
import requests


def check_grammar(input_str, language='en_US'):
    tool = language_tool_python.LanguageToolPublicAPI(language)
    matches = tool.check(input_str)
    is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    return language_tool_python.utils.correct(input_str, matches)




