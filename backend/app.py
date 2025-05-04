from flask import Flask
from flask_cors import CORS
from models import db, init_db
from routes import api

app = Flask(__name__)
CORS(app)

# Configure SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "206-369-984"  # Needed for sessions

# Initialize DB
init_db(app)

# Register routes
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
