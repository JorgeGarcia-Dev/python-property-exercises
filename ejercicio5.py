"""Definimos la clase Lenguaje"""

class Languaje: 

    
    def __init__(self, nombre):
        
        """
        La función __init__() es una función especial en las clases de Python. Se ejecuta tan pronto como un objeto
        de una clase es instanciada. El método __init__() es similar a los constructores en C++ y Java.
        
        :param nombre de usuario: el nombre de usuario del usuario del que desea obtener la información.
        """
        
        self.__nombre = nombre
    
    
    @property
    def name(self):
        
        """
        La función nombre() devuelve el valor de la variable __nombre.
        :return: El nombre del objeto.
        """
        
        return self.__nombre 
    
    
    @name.setter 
    def name_edit(self, valor): 
        """
        La función name_edit() toma un parámetro llamado valor y establece el valor de la variable
        nombre al valor del parámetro valor.
        :param valor: El valor que se le asignará al atributo.
        """
        
        self.__nombre = valor

# Creando una instancia de la clase Lenguaje.
name = Languaje('Python')

# Llamar a la función name() de la clase Language.
leng = name.name
print (f"Mi lenguaje de programación es: {leng}")

# Reasignando el valor de la variable privada `__name` con el nuevo valor: "JavaScript"
name.name_edit = "JavaScript"
print(f"Mi otro lenguaje de programación es: {name.name_edit}")