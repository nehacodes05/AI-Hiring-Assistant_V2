from flask import Flask
from routes.auth import auth_bp

app = Flask(__name__)  # creates your flask application

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
