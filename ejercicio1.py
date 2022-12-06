"""Definimos la clase Lenguaje"""

class Clase:
    def __init__(self, mi_atributo):
        
        """
        La función __init__() es una función especial en las clases de Python. Se ejecuta tan pronto como un objeto
        de una clase es instanciada. El método __init__() es similar a los constructores en C++ y Java.
        
        :param nombre de usuario: el nombre de usuario del usuario del que desea obtener la información.
        """
        
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        
        # El acceso se realiza a través de este "método" y
        # podría contener código extra y no un simple retorno.
        
        return self.__mi_atributo

saludo = Clase("Hola desde un Decorador.")
print(saludo.mi_atributo)