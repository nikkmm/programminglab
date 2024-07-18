class Studente:
# attributo uguale per tutti
ruolo = "Studente UNITS"
# costruttore, per ogni studente,
# che permette di creare un oggetto
# della classe, con opportuni valori per
# eventuali variabili di istanza dell'oggetto Studente
def __init__(self, nome, cognome):
self.nome = nome
self.cognome = cognome
def bonjour(self):
print(self.ruolo, ":", self.nome, self.cognome)




class A:
x = 0
y = ""
def __init__(self, n, s):
self.x = n
self.y = s
myObject = MyClass(12345, "Hello")
print(myObject.__str__()) # <__main__.MyClass object at 0x7f66d12bd1f0>
print(myObject.__repr__()) # <__main__.MyClass object at 0x7f66d12bd1f0>
print(myObject) # <__main__.MyClass object at 0x7f66d12bd1f0>
Usando il metodo magico __str__
class A:
x = 0
y = ""
def __init__(self, n, s):
self.x = n
self.y = s
def __str__ (self):
return 'A(x=' + str(self.x) + ' , y=' + self.y + ')'
myObject = A(12345, "Hello")
print(myObject.__str__()) # A(x=12345 , y=Hello)
print(myObject) # A(x=12345 , y=Hello)
print(str(myObject)) # A(x=12345 , y=Hello)



# creo un oggetto e chiamo la funzione bonjour
obj_Giulio = Studente("Giulio", "Caravagna")
obj_Giulio.bonjour()
# accedo al campo nome (come nelle struct in C)
print("Campo nome di Giulio", obj_Giulio.nome)
obj_Giulio.nome = "Giuliano" # cambio nome
print("Campo nome di Giulio", obj_Giulio.nome)
obj_Giulio.ruolo = "Bidello" # cambio ruolo
obj_Giulio.bonjour()