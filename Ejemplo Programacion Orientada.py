class persona:

    def __init__(self, edad, peso, estatura, nombre):
        self.__edad = edad
        self.__peso = peso
        self.__estatura = estatura
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def peso(self):
        return self.__peso
    
    @edad.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def estatura(self):
        return self.__estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self.__estatura = estatura

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    def __str__(self):
        return ("El nombre es: " + self.__nombre + "Tiene: " + str(self.__edad) 
                + "años" + "su estatura y peso son: " + str(self.__estatura) 
                + "y" + str(self.__peso) + "Kg")

santi = persona(35, 96, 1.82, "Santi")
print(santi)
