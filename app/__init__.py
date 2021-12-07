from flask import Flask

app = Flask(__name__)

from app import views
from app import GCP_Finder
from app import GroundControlPoint
from app import Image_
from app import Statistics


if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(f'ENV is set to: {app.config["ENV"]}')

 

