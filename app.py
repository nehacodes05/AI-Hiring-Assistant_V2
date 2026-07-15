from flask import Flask
from routes.auth import auth_bp
from routes.jobs import jobs_bp
from routes.applications import applications_bp

app = Flask(__name__)  # creates your flask application

app.register_blueprint(auth_bp)

app.register_blueprint(jobs_bp)

app.register_blueprint(applications_bp)


if __name__ == "__main__":
    app.run(debug=True)
