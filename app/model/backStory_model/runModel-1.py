import os
from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
import re


tokenizer_file = "aitextgen.tokenizer.json"

ai = aitextgen(model_folder="trained_model", tokenizer_file=tokenizer_file)
results = ai.generate(1, prompt="He is", include_prefix=False, max_length=400, return_as_list=True)
print(results)
# Process machine output

final = []
for x in results:
    final.append(x.split("\n")[0])
print(final,"final")

print("\n"*2)

texts = []
for x in final:
    startIndex, endIndex = [periodObj for periodObj in re.finditer('\.', x)][-1].span()
    texts.append(x[:endIndex])

print(texts)