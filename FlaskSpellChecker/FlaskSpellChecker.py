
from datetime import datetime
from flask import render_template,  make_response, Response
from flask import Flask
from lang_helper import sinhala
from nltk import grammar, parse
from flask import request
import json
import string
import numpy as np

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    try:
        # Read the Sinhala Grammar
        singram = grammar.FeatureGrammar.fromstring(sinhala)
        parser = parse.FeatureEarleyChartParser(singram)
        # strLine = "මිනිස්සු කුරුල්ලන් ලගින ගස කපති"
        # strLine = request.form["text"]
        strLine = request.json['InputText']
        tokens = strLine.split()
        trees = parser.parse(tokens)

        chkStrgFirst = "Test"
        chkStrgFinal = "Test"

        sentenceSize = []

        print(len(tokens))

        if len(tokens) == 2:
            i = 0
            for tree in trees:
                for node in tree:

                    for nodenode in node:
                        print(str(node))
                        if i == 0:
                            chkStrgFirst = str(nodenode)
                            print(str(nodenode) + '\n')
                        i = i + 1
                        chkStrgFinal = str(nodenode)

        if len(tokens) == 3:
            i = 0
            for tree in trees:

                for node in tree:

                    for nodenode in node:
                        if i == 0:
                            chkStrgFirst = str(nodenode)
                            print(str(nodenode) + '\n')
                        i = i + 1
                        chkStrgFinal = str(nodenode)

        if len(tokens) == 4:
            i = 0
            for tree in trees:
                for node in tree:

                    for nodenode in node:

                        if i == 0:
                            chkStrgFirst = str(nodenode)
                            print(str(nodenode) + '\n')
                        i = i + 1
                        chkStrgFinal = str(nodenode)

        print(chkStrgFirst)
        print(chkStrgFinal)

        chkStrgFirstArry = chkStrgFirst.split("[")
        chkStrgFirst = chkStrgFirstArry[1]
        chkStrgFirstArry = chkStrgFirst.split("]")
        chkStrgFirst = chkStrgFirstArry[0]
        print(chkStrgFirst)

        print("++++++++++++++")

        chkStrgFinalArry = chkStrgFinal.split("[")
        chkStrgFinal = chkStrgFinalArry[1]
        chkStrgFinalArry = chkStrgFinal.split("]")
        chkStrgFinal = chkStrgFinalArry[0]
        print(chkStrgFinal)

        jstre = json.dumps(tree)
        jsting = json.loads(jstre)
        newstr = str(jsting)
        newstr02 = newstr.replace("[", "")
        newstr03 = newstr02.replace("]", "")
        print(newstr03)

        tense = "test"
        singular_plural = "test"
        gramr = "correct grammer"

        if "TENSE='Npast'" in chkStrgFinal:
            tense = "present"
        if "TENSE='past'" in chkStrgFinal:
            tense = "past"
        if "NUM='pl'" in chkStrgFirst and "NUM='pl'" in chkStrgFinal:
            singular_plural = "plural"
        if "NUM='sg'" in chkStrgFirst and "NUM='sg'" in chkStrgFinal:
            singular_plural = "singular"
        if tense == "test" or singular_plural == "test":
            gramr = "wrong grammer"

        #print(sentenceSize)

        jObj = {}
        jObj["gramr"] = gramr
        jObj["tense"] = tense
        jObj["singular_plural"] = singular_plural

    except:
        tense = "test"
        singular_plural = "test"
        gramr = "wrong grammer"
        jObj = {}
        jObj["gramr"] = gramr
        jObj["tense"] = tense
        jObj["singular_plural"] = singular_plural

    return Response(json.dumps(jObj), mimetype='application/json')


@app.route('/ajax', methods=['GET', 'POST'])
def res_massage():
    return "The Corrected Sentence"


if __name__ == '__main__':
    app.run(port=50000, debug=True)
