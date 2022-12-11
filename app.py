import utils
from flask import Flask

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
    candidates = utils.get_all("candidates.json")
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'

@app.route('/candidates/<int:pk>')
def get_data(pk):
    candidates = utils.get_by_pk(pk)
    if not candidates:
        return "Кандидат не найден!"
    result = '<br>'
    result += candidates['name'] + '<br>'
    result += candidates['position'] + '<br>'
    result += candidates['skills'] + '<br>'
    result += '<br>'

    return f'''
         <img src="{candidates['picture']}">
         <pre>{result} </pre>
    '''

@app.route('/candidates/<skills>')
def get_skill(skills):
    candidates = utils.get_by_skill(skills)
    for candidate in candidates:

        result = '<br>'
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'

if __name__ == '__main__':
    app.run()
