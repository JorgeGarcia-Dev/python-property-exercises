![Banner Python](images/Banner_Python.png)

# Decorador @property en Python

El decorador @property es un decorador incorporado para la función property() en Python. Se usa para asignarle una funcionalidad "especial" a ciertos métodos para que actúen como "getters", "setters" o "deleters" al momento de definir y usar propiedades en una clase.

---

* **Podemos definir 3 métodos para una propiedad:**
  * **getter:** Para acceder al valor del atributo.
  * **setter:** Para actualizar el valor del atributo.
  * **deleter:** Para eliminar el atributo de la instancia.

---

**Ejemplo:**

```
class Clase:

    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

saludo = Clase("Hola desde un Decorador.")
print(saludo.mi_atributo)
```

---

**Nota:**

Se hace uso del método "getter" al decorar nuestra función con @property, por lo que no hace falta nombrarlo como en el caso de "setter" y "deleter", en donde tenemos que nombrar a la función junto con el método.

* **getter**

```
@property 
def nombre(self):
    return self.__nombre
```

* **setter**

```
@nombre.setter 
def nombre(self, valor):
    self.__nombre = valor
```

* **deleter**
```
@nombre.deleter 
def nombre(self):
    del self.__nombre
```