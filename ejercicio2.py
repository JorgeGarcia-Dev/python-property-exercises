"""Definimos la clase Empleados"""

class Empleados:
    
    def __init__(self, name, clave):
        """
        La función __init__() es una función especial en las clases de Python. Se ejecuta tan pronto como un objeto
        de una clase es instanciada. El método es útil para hacer cualquier inicialización que quieras hacer con
        tu objeto.
        
        :param name: Este es el nombre de la clase
        :param clave: Este es el nombre del atributo
        """
        
        self.name = name
        self.__clave = clave
    
    @property
    def key(self):
        
        """
        El método `key` devuelve el valor de la variable privada `__clave`
        :return: La clave del objeto.
        """
        
        return self.__clave
    
    @key.setter
    def key(self, value):
        
        """
        La función setter nos permite establecer el valor del atributo
        :param value: El valor que se pasa al método setter.
        """
        
        self.__clave = value

# Creando un objeto de la clase Empleados.
em = Empleados("Jorge", "jor632023")


print(em.key)
print(em.name)
# Reasignando el valor de la variable privada `__clave` con el nuevo valor: "JORGE2099"
em.key = "JORGE2099"
print(em.key)