from flask import Flask, render_template, request
from utils import get_base_url
from aitextgen import aitextgen
import re
app = Flask(__name__)

port = 12345
base_url = get_base_url(port)

@app.route(f'{base_url}')
def home():
    return render_template('home.html')

@app.route(f'{base_url}/about')
def about():
    return render_template('about.html')

@app.route(f'{base_url}/playground', methods=['POST', 'GET'])
def playground():
    final = ""
    model = "backstory"
    prompt = ""
    randomness = ""
    output = ""
    if request.method == 'POST':
        model = request.form['generate-type']
        prompt = request.form['user-prompt']
        randomness = float(request.form['randomness']) / 100
        print(randomness)
        if (model=="personality"):
            if prompt == "":
                prompt = "They" #sets default personality prompt to "They"
            ai = aitextgen(model_folder="model/trained_model/personality_model/", tokenizer_file="model/personality_model/aitextgen.tokenizer.json", to_gpu=False)
            a = ai.generate(4, max_length=100, include_prefix=False, prompt=prompt, return_as_list = True, temperature=randomness)# seperator
            final = []
            for x in a:
                final.append(x.split("\n")[0])
            print(final)
            output = final

        elif (model == "backstory"):
            ai = aitextgen(model_folder="model/backStory_model/", tokenizer_file="model/backStory_model/aitextgen.tokenizer.json", to_gpu=False)
            results = ai.generate(4, max_length=100, include_prefix=False, prompt=prompt, return_as_list=True, temperature=randomness)
            # seperator
            final = []
            for x in results:
                final.append(x.split("\n")[0])
            texts = []
            for x in final:
                startIndex, endIndex = [periodObj for periodObj in re.finditer('\.', x)][-1].span()
                texts.append(x[:endIndex])
            print(texts)
            output = texts
        elif (model=="physical"):
            ai = aitextgen(model_folder="model/physical_Model/", tokenizer_file="model/physical_Model/aitextgen.tokenizer.json", to_gpu=False)
            a = ai.generate(4, max_length=100, include_prefix=False, prompt=prompt, return_as_list = True, temperature=randomness,
            truncate='<EOS>')# seperator
            final = []
            for x in a:
                final.append(x.split("\n")[0])
            print(final)
            output = final

        return render_template('playground.html', output=output)
    else:
        return render_template('playground.html')



if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc9.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
