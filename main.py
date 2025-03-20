from flask import Flask
from config import Config
from db import db
from routes import routes
from flask_migrate import Migrate
from models import URL

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate = Migrate(app, db)



app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
