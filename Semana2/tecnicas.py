 #Abstraccion
from abc import ABC, abstractmethod

class maquina_de_cafe():
    @abstractmethod
    def preparar_bebida(self):
        pass

class Cafe(maquina_de_cafe):
    def preparar_bebida(self):
        print("Preparando el café: calentando agua, filtrando café. Ya esta listo el café")

class Te(maquina_de_cafe):
    def preparar_bebida(self):
        print("Preparando té: calentando agua, infusionando té. Ya esta listo el té")


bebidas = [Cafe(), Te()]
for bebida in bebidas:
    bebida.preparar_bebida()
print(f'----------------------------------------------------------------------------')
#Encapsulamiento
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Monto inválido o saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(200)
cuenta.depositar(40)
cuenta.retirar(50)
print(f"Saldo actual: {cuenta.consultar_saldo()}")
print(f'----------------------------------------------------------------------------')
#Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

class Lobo(Animal):
    def hablar(self):
        return "Auuuuu Auuuuu"

class Pollo(Animal):
    def hablar(self):
        return "Pio pio"

animales = [Lobo("Aska"), Pollo("Cantarito")]
for animal in animales:
    print(f"{animal.nombre} dice: {animal.hablar()}")

print(f'----------------------------------------------------------------------------')

# Polimorfismo
class Instrumento:   # Esta es una clase
    def tocar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

class Guitarra(Instrumento):
    def tocar(self):
        return "La guitarra suena: ¡strum strum!"

class Piano(Instrumento):
    def tocar(self):
        return "El piano suena: ¡plink plonk!"

class Flauta(Instrumento):
    def tocar(self):
        return "La flauta suena: ¡fiuuu fiuuu!"

class Bateria(Instrumento):
    def tocar(self):
        return "La batería suena: ¡boom bam!"

#Ejecucion 
instrumentos = [Guitarra(), Piano(), Flauta(), Bateria()]
for instrumento in instrumentos:
    print(instrumento.tocar())
