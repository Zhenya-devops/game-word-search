import re

from flask import Flask
from flask import render_template, jsonify, request

from guess import Guess
from maw import Analysis
from constants import REGEX

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    result = {}
    phrase = ''
    if request.method == 'POST':
        phrase = str(request.form['text_words'])
        result_maw = _maw.morphological_analysis_text_and_converter(f"{str(request.form['text_words'])}")
        results_guess = _guess.guess_world(result_maw)

        for name, percentage in results_guess.items():
            new_name = re.search(REGEX, name)
            result[new_name.group(0)] = float(f'{percentage * 100:.2f}')

    return render_template('index.html', results_guess=result, phrase=phrase)


@app.route('/api')
def api():
    results_guess = {"Test": 1, "Text": 2}
    return render_template('api.html', results_guess=results_guess)


@app.route('/api/guess/result', methods=['GET'])
def get_result():
    data = request.get_json()
    world: str = data["text"]

    result_maw = _maw.morphological_analysis_text_and_converter(f"{world}")
    results_guess = _guess.guess_world(result_maw)

    return jsonify(results_guess)


if __name__ == '__main__':
    _guess = Guess()
    _maw = Analysis()
    app.config['JSON_AS_ASCII'] = False
    app.run()
