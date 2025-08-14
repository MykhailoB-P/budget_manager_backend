from flask import Flask
from flask_cors import CORS
from routes import api  # for import a blueprint

app = Flask(__name__)
CORS(app)

# Registering routes
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
