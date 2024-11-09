import configparser
import os

from app import create_app

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == '__main__':
    app = create_app()
    app.config['MONGO_URI'] = config['PROD']['DB_URI']
    app.run(debug=True)
