import os
from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU

tokenizer_file = "aitextgen.tokenizer.json"

ai = aitextgen(model_folder="trained_model", tokenizer_file=tokenizer_file)
results = ai.generate(1, prompt="He started as", include_prefix=False, max_length=400, return_as_list=True)
print(results)
# Process machine output


output=""
for x in results:
    output+=x
output=output.split()
#print(output)
for x in output:
    if "." in x:
        c=output.index(x)
print(" ".join(output[:c+1]))



#print("".join(x))
    #if (x.find(".")):
    #    print(x[:x.index(".")] + ".")
    
# Hello Mr. Raj! I just finished deleting the nonsentence parts!
#good work :) I will be there soon
# Here is the code!

#import re
#texts = []
#for x in final:
#    startIndex, endIndex = [periodObj for periodObj in re.finditer('\.', x)][-1].span()
#    texts.append(x[:endIndex])