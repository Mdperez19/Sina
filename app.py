from flask import Flask
from spellchecker.spellchecker_controller import spellchecker_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[
    'http://localhost:4200',
    'https://paradis-bnkur1wx4-aliss55s-projects.vercel.app/',
    'https://paradis-r9co4bjsb-aliss55s-projects.vercel.app/'
])
app.register_blueprint(spellchecker_api, url_prefix='/spellchecker')

if __name__ == '__main__':
    app.run(debug=True)
