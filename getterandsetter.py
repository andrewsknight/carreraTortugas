class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor):
        .__propiedad_privada = valor
    
    def getPropiedadPrivada(self):
        return self._propiedad_privada
        