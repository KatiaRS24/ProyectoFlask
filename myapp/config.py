class Config(object):#configura que nuestro servidor se active en modo debug o modo desarrollo.
    pass

class ProdConfig(Config):#
    pass

class DevConfig(Config):#
    DEBUG = True