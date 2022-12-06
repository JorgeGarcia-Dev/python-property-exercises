"""Definimos la clase User"""

class User:

    def __init__(self, username):
        
        """
        La función __init__() es una función especial en las clases de Python. Se ejecuta tan pronto como un objeto
        de una clase es instanciada. El método __init__() es similar a los constructores en C++ y Java.
        
        :param nombre de usuario: el nombre de usuario del usuario del que desea obtener la información.
        """

        self.__username = username
    
    @property
    def username(self):
        
        """
        La función `username` devuelve el valor de la variable privada `__username`
        :return: El nombre de usuario.
        """
        
        return self.__username
    
    @username.setter
    def username(self, value):
        
        """
        La función setter nos permite establecer el valor de la variable privada
        :param value: El valor que se le está asignando al atributo.
        """
        
        self.__username = value

# Creando una instancia de la clase User.
user = User("Jorge2023")
print(user.username)
# Cambia el nombre del parámetro `username` a `nuevo_username` enviándo y asignando nuevos valores.
nuevo_username = "JORge2099"
print(nuevo_username)