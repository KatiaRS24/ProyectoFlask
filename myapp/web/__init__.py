#Este archivoi se utiliza para realizar la importación de las configuraciones tales 
#como la importanción de la app

from flask import Flask

from myapp.config import DevConfig
from myapp.task.controllers import taskRoute

app = Flask(__name__) #Cres el objeto global de nuestra 
app.register_blueprint(taskRoute)#Registra la ruta del task

#app.debug = True
app.config.from_object(DevConfig)#Esta es la ruta más global del proyecto
@app.route('/')
def hello_world() -> str:
    return ' Hello world'