from flask import Flask
from myapp.config import DevConfig
from myapp.task.controllers import taskRoute

app = Flask(__name__)
app.register_blueprint(taskRoute)

#app.debug = True
app.config.from_object(DevConfig)


@app.route('/')
def hello_world() -> str:
    return ' Hello world'