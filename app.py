from flask import Flask
from spellchecker.spellchecker_controller import spellchecker_api

app = Flask(__name__)
app.register_blueprint(spellchecker_api, url_prefix='/spellchecker')

if __name__ == '__main__':
    app.run(debug=True)
