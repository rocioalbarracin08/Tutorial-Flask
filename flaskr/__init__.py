import os
from flask import Flask

#Contendrá la fábrica de la aplicación, y le dice a Python que el directorio flaskr debe ser tratado como un paquete.

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Cargue la configuración de la instancia, si existe, cuando no se esté probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog 
    app.register_blueprint(blog.bp) #Importa y registra el blueprint de la fábrica (Carpeta "flaskr")
    app.add_url_rule('/', endpoint='index')

    return app


    