import torch
import language_tool_python
import requests


def check_grammar(input_str, language='en_US'):
    tool = language_tool_python.LanguageToolPublicAPI(language)
    matches = tool.check(input_str)
    is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    return language_tool_python.utils.correct(input_str, matches)

sent = language_tool_python.utils.correct(input_str, matches)
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = T5Tokenizer.from_pretrained('deep-learning-analytics/GrammarCorrector')
model = T5ForConditionalGeneration.from_pretrained('deep-learning-analytics/GrammarCorrector').to(torch_device)

num_return_sequences = 1

def correct_grammar(input_text,num_return_sequences=num_return_sequences):
  batch = tokenizer([input_text],truncation=True,padding='max_length',max_length=64, return_tensors="pt").to(torch_device)
  results = model.generate(**batch,max_length=64,num_beams=2, num_return_sequences=num_return_sequences, temperature=1.5)
  #answer = tokenizer.batch_decode(results[0], skip_special_tokens=True)
  return results
  
##Prompts
results = correct_grammar(sent, num_return_sequences)


