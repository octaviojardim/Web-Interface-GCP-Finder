from flask import Flask

app = Flask(__name__)

from app import views
from app import _Controller
from app import _GroundControlPoint
from app import _Image
from app import _Statistics


if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(f'ENV is set to: {app.config["ENV"]}')

 

