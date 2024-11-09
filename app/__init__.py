from flask import Flask
from pymongo import MongoClient
import logging

from pymongo.server_api import ServerApi

from app.routes.user_routes import user_bp

# Initialize MongoClient outside of any function to allow for reusability
client = None
db = None


def create_app(config_class='config.base.BaseConfig'):
    global client, db

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)
    app.register_blueprint(user_bp, url_prefix='/users')

    # Check if the MONGO_URI is set in the config
    if 'MONGO_URI' not in app.config:
        app.logger.error('MONGO_URI is not set in config')
        return app  # Return early to avoid further issues

    uri = app.config['MONGO_URI']

    print(uri)
    # Connect to MongoDB using pymongo
    client = MongoClient(uri, server_api=ServerApi('1'))

    print("É agora que morre")
    # Access the specific database
    db = client.get_database()

    print("foi?")
    # Set up logging
    handler = logging.StreamHandler()  # Logs to the console
    handler.setLevel(logging.INFO)  # Log level can be adjusted to DEBUG, ERROR, etc.
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Ping MongoDB to check if it's working
    try:
        # Send a simple ping command to the database to check if the connection is alive
        client.admin.command('ping')
        app.logger.info("MongoDB is connected and working.")
    except Exception as e:
        app.logger.error(f"MongoDB connection failed: {e}")

    # Example of accessing a collection
    todos = db.todos  # The collection you want to work with

    return app
