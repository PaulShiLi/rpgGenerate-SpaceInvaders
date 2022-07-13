from flask import Flask, render_template, request
from utils import get_base_url
import re
from aitextgen import aitextgen
import os

# Get file paths
parentPath = os.getcwd()
templatePath = f"{parentPath}/templates"
staticPath = f"{parentPath}/static"
imgPath = f"{parentPath}/static/img"
machineModel = f"{parentPath}/model"

# Initialize Flask Object
app = Flask(__name__, template_folder=templatePath, static_folder=staticPath)

port = 12345
base_url = get_base_url(port)

@app.route(f'{base_url}')
def home():
    return render_template('home.html')

@app.route(f'{base_url}/playground', methods=['POST', 'GET'])
def playground():
    final = ""
    model = ""
    prompt = ""
    randomness = ""
    if request.method == 'POST':
        model = request.form['generate-type']
        prompt = request.form['user-prompt']
        randomness = float(request.form['randomness']) / 100
        print(randomness)
        if (model=="personality"):
            ai = aitextgen(model_folder=f"{machineModel}/personality_Model/trained_Model", tokenizer_file=f"{machineModel}/personality_Model/aitextgen.tokenizer.json", to_gpu=True)
            a = ai.generate(4, max_length=100, include_prefix=False, prompt=prompt, return_as_list = True, temperature=randomness)# seperator
            final = []
            for x in a:
                final.append(x.split("\n")[0])
            print(final)
        if model == "lore":
            ai = aitextgen(model_folder=f"{machineModel}/backStory_Model/trained_Model",
                      tokenizer_file=f"{machineModel}/backStory_Model/aitextgen.tokenizer.json", to_gpu=True)
            results = ai.generate(1, max_length=100, include_prefix=False, prompt=prompt, return_as_list=True,
                            temperature=randomness)  # seperator
            final = []
            for x in results:
                final.append(x.split("\n")[0])
            texts = []
            for x in final:
                startIndex, endIndex = [periodObj for periodObj in re.finditer('\.', x)][-1].span()
                texts.append(x[:endIndex])
            print(texts)

        # TO-DO Generate using ai
        output = final

        return render_template('playground.html', output=output)
    else:
        return render_template('playground.html')

@app.route(f'{base_url}/about')
def about():
    return render_template('extendAbout.html')

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc9.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
