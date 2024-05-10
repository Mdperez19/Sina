from flask import Flask
from spellchecker.spellchecker_controller import spellchecker_api
from flask_cors import CORS

app = Flask(__name__)
origins = [
    r"https://paradis-.*\.vercel\.app",  # Vercel subdomain
    r"http://localhost:4200"              # Localhost for development
]

# Enable CORS for all resources on this server
cors = CORS(app, resources={r"/*": {"origins": origins}})

app.register_blueprint(spellchecker_api, url_prefix='/spellchecker')

if __name__ == '__main__':
    app.run(debug=True)
