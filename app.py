from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from flask_migrate import Migrate
from Resource.Profile_Resource import ProfileResource  # Ensure this matches the renamed file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
jwt = JWTManager(app)
api = Api(app)
migrate = Migrate(app, db, render_as_batch=True)

# Register resources
api.add_resource(ProfileResource, '/profile')

if __name__ == '__main__':
    app.run(port=5000)
