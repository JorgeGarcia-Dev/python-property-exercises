"""Definimos la clase Rectangle"""

class Rectangulo:
    
    def __init__(self, width, height):
        
        """
        La función __init__() es una función especial en las clases de Python. Se ejecuta tan pronto como un objeto
        de una clase es instanciada. El método __init__() es similar a los constructores en C++ y Java.
        
        :param nombre de usuario: el nombre de usuario del usuario del que desea obtener la información.
        """
        
        self.width = width
        self.height = height
    
    @property
    def area(self):
        
        """
        Esta función toma un objeto de rectángulo y devuelve el área de ese rectángulo.
        :return: El área del rectángulo.
        """
        
        return self.width * self.height

# Creando una instancia de la clase Rectangulo.
rectangle = Rectangulo(30, 50)
# Llamar a la función de área de la clase Rectangulo.
result = rectangle.area
print(f"The result of the area is: {result}")